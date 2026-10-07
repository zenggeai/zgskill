#!/usr/bin/env python3
"""Local article preparation/checking and authorized WeChat draft delivery.
No public-publishing endpoint is implemented. Credentials stay in the config.
"""
import argparse
import copy
import hashlib
import html as html_module
import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

from bs4 import BeautifulSoup

SKILL = Path(__file__).resolve().parents[1]
GIFT = 'https://mp.weixin.qq.com/s/NQC0dF23hHz4v740WIa6tg'
PHRASES = ('点个赞、在看、转发', 'V:zengge198406。')
GAP_ENDS = ('让好内容被更多的人看到。', '企业工作流自动化。', '数字员工团队。')
CTA = '以上内容对你有启发，随手'


def normalize(text):
    return re.sub(r'[\s\u200b]+', '', text)


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    temp.replace(path)


def plain(fragment):
    return BeautifulSoup(fragment, 'html.parser').get_text()


def css_color(style):
    m = re.search(r'(?:^|;)\s*color\s*:\s*(#[0-9a-f]{6}|rgb\([^)]*\))', style, re.I)
    if not m:
        return ''
    value = m.group(1).lower()
    if value.startswith('rgb'):
        nums = re.findall(r'\d+', value)
        if len(nums) == 3:
            return '#' + ''.join(f'{int(x):02x}' for x in nums)
    return value


def footer_contract(fragment):
    soup = BeautifulSoup(fragment, 'html.parser')
    colors = {}
    for phrase in PHRASES:
        nodes = [n for n in soup.find_all('strong') if n.get_text() == phrase]
        if len(nodes) != 1 or not css_color(nodes[0].get('style', '')):
            raise ValueError('文末两处引导文字必须有明确的加粗颜色')
        colors[phrase] = css_color(nodes[0]['style'])
    gaps = []
    for empty in soup.find_all('p'):
        if not normalize(empty.get_text()) and empty.find('br'):
            previous = empty.find_previous_sibling()
            if previous is not None and previous.name == 'p':
                gaps.append(normalize(previous.get_text()))
    return {'text': normalize(soup.get_text()), 'colors': colors, 'gap_texts': gaps,
            'links': [{'text': a.get_text(strip=True), 'href': a.get('href', '')} for a in soup.find_all('a')]}


def inspect(fragment, sections, contract):
    soup = BeautifulSoup(fragment, 'html.parser')
    hs = soup.find_all('h2')
    imgs = soup.find_all('img')
    opening = ''
    if hs:
        # Walk the actual document order; images add no visible prose characters.
        for item in soup.descendants:
            if item is hs[0]:
                break
            if isinstance(item, str):
                opening += item
    checks = {'opening_within_200': len(normalize(opening)) <= 200 and bool(normalize(opening)),
              'section_count': len(hs) == sections}
    hrs = soup.find_all('hr')
    foot = BeautifulSoup(''.join(str(n) for n in hrs[-1].next_siblings), 'html.parser') if hrs else soup
    checks['footer_text'] = normalize(foot.get_text()) == contract['text']
    for phrase, color in contract['colors'].items():
        ns = [n for n in foot.find_all('strong') if n.get_text() == phrase]
        checks['style_' + phrase] = len(ns) == 1 and css_color(ns[0].get('style', '')) == color and bool(re.search(r'font-weight\s*:\s*(700|bold)', ns[0].get('style', ''), re.I))
    for i, text in enumerate(contract.get('gap_texts', [])):
        p = next((n for n in foot.find_all('p') if normalize(n.get_text()) == text), None)
        nxt = p.find_next_sibling() if p else None
        checks['footer_gap_' + str(i + 1)] = bool(nxt and nxt.name == 'p' and not normalize(nxt.get_text()) and nxt.find('br'))
    checks['image_count'] = len(imgs) == sections + 1
    checks['title_image_position'] = bool(imgs and hs and imgs[0].find_previous('h2') is None and imgs[0].find_next('h2') is hs[0])
    checks['section_image_positions'] = len(imgs) == sections + 1 and all(imgs[i + 1].find_previous('h2') is hs[i] for i in range(min(sections, len(hs))))
    return checks, len(normalize(opening))


def byte_digest(text, limit=120):
    return text.encode('utf-8')[:limit].decode('utf-8', errors='ignore')


def default_config():
    for name in ('wewrite', 'zg-wewrite'):
        path = SKILL.parent / name / 'config.yaml'
        if path.is_file():
            return str(path)
    return str(Path.home() / '.config' / 'wewrite' / 'config.yaml')


def render_body(markdown_text, theme_name):
    toolkit = next((SKILL.parent / name / 'toolkit' for name in ('wewrite', 'zg-wewrite') if (SKILL.parent / name / 'toolkit').is_dir()), None)
    if toolkit is not None:
        sys.path.insert(0, str(toolkit))
        from converter import WeChatConverter
        from theme import load_theme
        try:
            theme = load_theme(theme_name)
        except FileNotFoundError:
            theme = load_theme('professional-clean')
        result = WeChatConverter(theme=theme).convert(markdown_text)
        return result.html
    import markdown
    body = re.sub(r'^#\s+[^\n]+\n?', '', markdown_text, count=1)
    soup = BeautifulSoup(markdown.markdown(body, extensions=['extra']), 'html.parser')
    styles = {'p': 'font-size:16px;line-height:1.6;color:#222;margin:0 8px 12px',
              'h2': 'font-size:21px;line-height:1.5;color:#222;margin:28px 8px 14px;font-weight:700',
              'a': 'color:#406ADC;text-decoration:none'}
    for tag, style in styles.items():
        for n in soup.find_all(tag):
            n['style'] = style + ';' + n.get('style', '')
    return str(soup)


def prepare(args):
    md = Path(args.markdown).resolve()
    text = md.read_text(encoding='utf-8')
    m = re.search(r'^#\s+(.+)$', text, re.M)
    if not m:
        raise ValueError('Markdown需要一个完整H1原标题')
    title = m.group(1).strip()
    if args.title is not None and args.title != title:
        raise ValueError('源标题与用户原标题不一致；工具不会自行改题')
    # Strip only a recognized author footer, preventing duplicate append.
    matches = list(re.finditer(r'(?m)^(?:<p\b[^>]*>)?' + re.escape(CTA), text))
    if matches and '我是曾哥，AI一人公司获客系统创始人。' in text[matches[-1].start():]:
        text = text[:matches[-1].start()].rstrip()
        text = re.sub(r'\n\s*---\s*$', '', text).rstrip()
    footer = Path(args.footer).read_text(encoding='utf-8') if args.footer else (SKILL / 'assets/footer.html').read_text(encoding='utf-8')
    contract = footer_contract(footer)
    soup = BeautifulSoup(render_body(text, args.theme), 'html.parser')
    for im in soup.find_all('img'):
        im['style'] = 'width:100%;max-width:100%;height:auto;display:block;margin:0 auto'
        if im.parent.name in ('p', 'section'):
            im.parent['style'] = 'margin:0 8px 12px;padding:0'
    body = str(soup) + '\n' + footer
    checks, count = inspect(body, args.sections, contract)
    if not checks['opening_within_200']:
        raise ValueError(f'开头{count}字，必须为1—200字（含标点，不含空白）')
    if not checks['section_count']:
        raise ValueError('小节数量与指定结构不一致')
    if not all(v for k, v in checks.items() if k.startswith(('footer', 'style_', 'gap_'))):
        raise ValueError('固定文末或留白不符合要求')
    output = Path(args.outdir).resolve()
    output.mkdir(parents=True, exist_ok=True)
    manifest_path = output / 'article.manifest.json'
    if manifest_path.exists() and read_json(manifest_path).get('title') != title:
        raise ValueError('此输出目录已有另一篇文章，请为新标题使用新目录')
    body_path = output / 'article.body.html'
    body_path.write_text(body, encoding='utf-8')
    assets = []
    preview = BeautifulSoup(body, 'html.parser')
    for im, pre in zip(BeautifulSoup(body, 'html.parser').find_all('img'), preview.find_all('img')):
        src = im.get('src', im.get('data-src', ''))
        if src.startswith(('http://', 'https://')):
            assets.append({'src': src, 'remote': True})
        else:
            local = Path(unquote(urlparse(src).path)) if src.startswith('file:') else Path(src)
            local = local if local.is_absolute() else md.parent / local
            local = local.resolve()
            assets.append({'src': src, 'path': str(local), 'remote': False})
            pre['src'] = local.as_uri()
    preview_path = output / 'article.preview.html'
    preview_path.write_text('<!doctype html><html><head><meta charset="utf-8"><title>' + html_module.escape(title) + '</title></head><body style="max-width:720px;margin:28px auto;padding:0 16px;font-family:Arial,PingFang SC,sans-serif"><h1>' + html_module.escape(title) + '</h1>' + str(preview) + '</body></html>', encoding='utf-8')
    digest = args.digest if args.digest is not None else byte_digest(normalize(plain(str(soup))))
    if len(digest.encode('utf-8')) > 120:
        raise ValueError('摘要超过120个UTF-8字节，请缩短摘要')
    manifest = {'schema': 1, 'title': title, 'author': getattr(args, 'author', '曾哥'), 'digest': digest,
                'markdown': str(md), 'body_html': str(body_path), 'preview': str(preview_path),
                'cover': str(Path(args.cover).resolve()) if args.cover else None,
                'assets': assets, 'sections': args.sections, 'opening_chars': count,
                'footer_contract': contract, 'receipt': str(output / 'article.receipt.json')}
    write_json(manifest_path, manifest)
    return {'prepared': True, 'opening_chars': count, 'manifest': str(manifest_path),
            'preview': str(preview_path), 'checks': checks, 'ready_for_upload': all(checks.values()) and bool(manifest['cover'])}


class ApiError(ValueError):
    pass


class NetworkFailure(ValueError):
    pass


class WeChat:
    def __init__(self, config, session=None):
        import requests
        import yaml
        cfg = yaml.safe_load(Path(config).read_text(encoding='utf-8')) or {}
        credentials = cfg.get('wechat', {})
        self.appid, self.secret = credentials.get('appid'), credentials.get('secret')
        if not self.appid or not self.secret:
            raise ValueError('公众号配置缺少wechat.appid或wechat.secret')
        self.session = session or requests.Session()
        self.token = None

    def decode(self, response, stage):
        try:
            response.raise_for_status()
            response.encoding = 'utf-8'
            data = response.json()
        except Exception:
            raise NetworkFailure(f'{stage}未取得可靠响应；请检查连接或回读结果') from None
        if data.get('errcode', 0):
            message = str(data.get('errmsg', ''))
            for secret in (self.appid, self.secret, self.token):
                if secret:
                    message = message.replace(secret, '[REDACTED]')
            message = re.sub(r'access_token=[^\s&]+', 'access_token=[REDACTED]', message)
            raise ApiError(f'WeChat {stage} errcode={data["errcode"]}: {message}')
        return data

    def authenticate(self):
        if self.token:
            return
        try:
            response = self.session.get('https://api.weixin.qq.com/cgi-bin/token', params={'grant_type': 'client_credential', 'appid': self.appid, 'secret': self.secret}, timeout=30)
        except Exception:
            raise NetworkFailure('公众号认证请求未取得可靠响应') from None
        self.token = self.decode(response, 'token').get('access_token')
        if not self.token:
            raise NetworkFailure('公众号认证未返回token')

    def api(self, endpoint, payload):
        self.authenticate()
        try:
            response = self.session.post('https://api.weixin.qq.com/cgi-bin/' + endpoint, params={'access_token': self.token}, data=json.dumps(payload, ensure_ascii=False).encode('utf-8'), headers={'Content-Type': 'application/json; charset=utf-8'}, timeout=30)
        except Exception:
            raise NetworkFailure(f'{endpoint}未取得可靠响应') from None
        return self.decode(response, endpoint)

    def upload(self, path, cover=False):
        self.authenticate()
        endpoint = 'material/add_material' if cover else 'media/uploadimg'
        params = {'access_token': self.token}
        if cover:
            params['type'] = 'image'
        try:
            with Path(path).open('rb') as f:
                response = self.session.post('https://api.weixin.qq.com/cgi-bin/' + endpoint, params=params, files={'media': (Path(path).name, f)}, timeout=30)
        except Exception:
            raise NetworkFailure(f'{endpoint}未取得可靠响应') from None
        result = self.decode(response, endpoint)
        if not result.get('media_id' if cover else 'url'):
            raise NetworkFailure(f'{endpoint}没有返回素材标识')
        return result


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def preflight(manifest):
    fragment = Path(manifest['body_html']).read_text(encoding='utf-8')
    checks, count = inspect(fragment, manifest['sections'], manifest['footer_contract'])
    if not all(checks.values()):
        raise ValueError('文章预检未通过：' + '、'.join(k for k, v in checks.items() if not v))
    current_sources = [n.get('src', n.get('data-src', '')) for n in BeautifulSoup(fragment, 'html.parser').find_all('img')]
    if current_sources != [a['src'] for a in manifest['assets']]:
        raise ValueError('图片引用已变化，请重新prepare生成对应manifest')
    for asset in manifest['assets']:
        if asset['remote']:
            if urlparse(asset['src']).hostname != 'mmbiz.qpic.cn':
                raise ValueError('正文远端图片必须先上传微信图床；其他来源不能直接保存')
        elif not Path(asset['path']).is_file():
            raise ValueError('缺少正文图片：' + asset['path'])
    return fragment, checks, count


def verify_record(manifest, receipt, client):
    mid = receipt.get('media_id')
    if not mid:
        raise ValueError('没有可回读的media_id')
    data = client.api('draft/get', {'media_id': mid})
    news = data.get('news_item', [])
    if not news:
        raise ValueError('草稿回读没有文章')
    article = news[0]
    expected = Path(receipt['expected_html']).read_text(encoding='utf-8')
    actual = article.get('content', '')
    soup = BeautifulSoup(actual, 'html.parser')
    checks, count = inspect(actual, manifest['sections'], manifest['footer_contract'])
    checks.update(title=article.get('title') == manifest['title'], author=article.get('author') == manifest['author'], digest=article.get('digest') == manifest['digest'], body=normalize(plain(actual)) == normalize(plain(expected)), hosted_images=all(urlparse(im.get('src') or im.get('data-src', '')).hostname == 'mmbiz.qpic.cn' for im in soup.find_all('img')), cover=bool(article.get('thumb_media_id') == receipt.get('cover_media_id') or article.get('thumb_url')))
    link_checks = []
    for expected_link in manifest['footer_contract'].get('links', []):
        links = [a for a in soup.find_all('a') if a.get_text(strip=True) == expected_link['text']]
        ok = False
        if len(links) == 1:
            actual_link = links[0].get('href', '')
            parsed = urlparse(actual_link)
            query = parse_qs(parsed.query)
            source = urlparse(expected_link['href'])
            ok = actual_link == expected_link['href'] or source.hostname == 'mp.weixin.qq.com' and parsed.hostname == 'mp.weixin.qq.com' and parsed.path == '/s' and all(query.get(k) for k in ('__biz', 'mid', 'idx', 'sn'))
        link_checks.append(ok)
    checks['footer_links'] = all(link_checks)
    receipt.update(status='verified' if all(checks.values()) else 'needs_review', draft_verified=all(checks.values()), checks=checks, opening_chars=count, published=False)
    receipt.pop('error', None)
    write_json(manifest['receipt'], receipt)
    Path(manifest['body_html']).with_name('article.readback.html').write_text(actual, encoding='utf-8')
    return {'draft_saved': True, 'draft_verified': all(checks.values()), 'media_id': mid, 'published': False, 'checks': checks}


def save_draft(manifest, client, media_id=None):
    # All local validation precedes authentication or external mutation.
    fragment, _, _ = preflight(manifest)
    path = Path(manifest['receipt'])
    receipt = read_json(path) if path.exists() else {}
    if receipt.get('title') and receipt['title'] != manifest['title']:
        raise ValueError('此回执属于另一原标题，不能自动复用')
    if media_id and receipt.get('media_id') and media_id != receipt['media_id']:
        raise ValueError('指定ID与现有回执不一致，请先核对目标草稿')
    mid = media_id or receipt.get('media_id')
    if receipt.get('status') == 'creation_outcome_unknown' and not mid:
        raise ValueError('前次创建结果不确定；先定位已有草稿并绑定ID，不能盲目再次创建')
    if not manifest.get('cover') and not receipt.get('cover_media_id'):
        raise ValueError('新草稿需要封面图片')
    if manifest.get('cover') and not Path(manifest['cover']).is_file():
        raise ValueError('封面文件不存在')
    receipt.update(title=manifest['title'], draft_verified=False, published=False)
    try:
        old = client.api('draft/get', {'media_id': mid})['news_item'][0] if mid else {}
        uploads = receipt.get('image_uploads', {})
        for asset in manifest['assets']:
            if asset['remote']:
                continue
            fingerprint = sha(asset['path'])
            cached = uploads.get(asset['src'], {})
            url = cached['url'] if cached.get('sha256') == fingerprint else client.upload(asset['path'])['url']
            uploads[asset['src']] = {'sha256': fingerprint, 'url': url}
            fragment = fragment.replace(asset['src'], url)
        receipt['image_uploads'] = uploads
        if manifest.get('cover'):
            cover_sha = sha(manifest['cover'])
            if receipt.get('cover_sha256') != cover_sha or not receipt.get('cover_media_id'):
                cover = client.upload(manifest['cover'], cover=True)
                receipt.update(cover_media_id=cover['media_id'], cover_sha256=cover_sha)
        expected_path = Path(manifest['body_html']).with_name('article.saved.html')
        expected_path.write_text(fragment, encoding='utf-8')
        receipt['expected_html'] = str(expected_path)
        article = {k: old[k] for k in ('content_source_url', 'need_open_comment', 'only_fans_can_comment') if k in old}
        article.update(title=manifest['title'], author=manifest['author'], digest=manifest['digest'], content=fragment, thumb_media_id=receipt['cover_media_id'], show_cover_pic=0)
        if mid:
            receipt['media_id'] = mid
            client.api('draft/update', {'media_id': mid, 'index': 0, 'articles': article})
        else:
            try:
                result = client.api('draft/add', {'articles': [article]})
                if not result.get('media_id'):
                    raise NetworkFailure('草稿创建没有返回可记录的ID')
            except NetworkFailure:
                receipt['status'] = 'creation_outcome_unknown'
                write_json(path, receipt)
                raise
            mid = result['media_id']
            receipt['media_id'] = mid
        receipt['status'] = 'saved_pending_readback'
        write_json(path, receipt)  # Persist the ID before any verification call.
        return verify_record(manifest, receipt, client)
    except (ApiError, NetworkFailure, ValueError) as exc:
        if receipt.get('status') != 'creation_outcome_unknown':
            receipt['status'] = 'saved_needs_verification' if receipt.get('media_id') else 'save_failed'
        receipt['error'] = str(exc)
        write_json(path, receipt)
        raise


def parser():
    p = argparse.ArgumentParser(description='曾哥公众号本地排版、检查与获授权的草稿保存；不提供公开发布功能')
    sub = p.add_subparsers(dest='command', required=True)
    prepare_p = sub.add_parser('prepare', help='本地生成正文、预览和manifest，不调用微信')
    prepare_p.add_argument('--markdown', required=True)
    prepare_p.add_argument('--outdir', required=True)
    prepare_p.add_argument('--title', help='校验原标题，不能用来改题')
    prepare_p.add_argument('--author', default='曾哥', help='与本次文末一致的作者署名')
    prepare_p.add_argument('--digest')
    prepare_p.add_argument('--cover')
    prepare_p.add_argument('--footer', help='本次用户明确覆盖的文末HTML模板')
    prepare_p.add_argument('--sections', type=int, default=3)
    prepare_p.add_argument('--theme', default='learned-mp-xf3c60j')
    for name in ('check', 'draft', 'verify'):
        command = sub.add_parser(name)
        command.add_argument('--manifest', required=True)
        if name != 'check':
            command.add_argument('--config', default=default_config())
        if name == 'draft':
            command.add_argument('--media-id', help='用户明确指定的既有草稿ID')
    return p


def main():
    args = parser().parse_args()
    try:
        if args.command == 'prepare':
            result = prepare(args)
        else:
            manifest = read_json(args.manifest)
            if args.command == 'check':
                _, checks, count = preflight(manifest)
                result = {'checked': True, 'opening_chars': count, 'checks': checks}
            else:
                client = WeChat(args.config)
                result = save_draft(manifest, client, args.media_id) if args.command == 'draft' else verify_record(manifest, read_json(manifest['receipt']), client)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result.get('draft_verified', True) else 2
    except (ValueError, OSError, KeyError) as exc:
        # Network diagnostics are sanitized inside WeChat; no tracebacks with URLs/tokens.
        print(json.dumps({'completed': False, 'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
