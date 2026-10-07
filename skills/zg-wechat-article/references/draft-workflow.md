# 本地排版与公众号草稿交付

## 使用工具

本Skill的`article_tools.py`用于本地生成、检查，以及在已经获授权时创建或更新微信草稿。运行`--help`查看参数。依赖`markdown`、`beautifulsoup4`、`requests`、`PyYAML`；排版优先调用同级WeWrite的主题，缺失时使用基础内联排版。图像生成和编辑仍使用imagegen，工具不会替你生成图片。

先将已审阅正文写成Markdown：第一行是完整H1原标题，三个正文小节使用H2；标题图在首个H2之前，各正文图在对应小节末尾。Markdown中图片路径相对该Markdown文件。固定文末由工具追加，避免手动重复。曾哥以外的作者需先准备自己的文末HTML，再用`--footer`和`--author`传入；默认署名与固定文末都是曾哥的品牌预设。

```bash
python3 "<skill-dir>/scripts/article_tools.py" prepare \
  --markdown "/absolute/path/article.md" \
  --outdir "/absolute/path/outputs" \
  --cover "/absolute/path/title-scene.jpg" \
  --title "用户已选定的完整原标题"
```

生成`article.body.html`、`article.preview.html`和`article.manifest.json`。`--title`用于校验用户标题，不会替换源标题。未完成配图时可以先prepare供审阅；保存草稿前须补齐与小节数量匹配的图片和封面。用户另定小节数量可用`--sections`调整；不要为了凑数量拆空小节。

检查：

```bash
python3 "<skill-dir>/scripts/article_tools.py" check \
  --manifest "/absolute/path/outputs/article.manifest.json"
```

用户授权保存后：

```bash
python3 "<skill-dir>/scripts/article_tools.py" draft \
  --manifest "/absolute/path/outputs/article.manifest.json"
```

默认依次查找同级`wewrite/config.yaml`、`zg-wewrite/config.yaml`和用户目录下的`.config/wewrite/config.yaml`；也可以用`--config`显式指定自己已有的本地配置。公开安装包不包含任何公众号账号配置。另一个账户必须有用户明确指定。配置字段沿用`wechat.appid`、`wechat.secret`，无需在命令中粘贴密钥。

工具在草稿创建后立即写`article.receipt.json`。再次对同一manifest执行draft，会更新回执中的同一`media_id`。用户已明确指定既有草稿时可用`--media-id`，不要猜测或复用其他文章ID。

只回读：

```bash
python3 "<skill-dir>/scripts/article_tools.py" verify \
  --manifest "/absolute/path/outputs/article.manifest.json"
```

## 修改当前草稿

小范围修改时优先从云端回读当前稿，保留其中人工编辑的内容，然后用获授权的接口精确修改并更新同一个ID。不要用一份过时Markdown整篇覆盖最新草稿。同步修改本地可编辑源与预览。

微信可能把图像外层`p`转成`section`，把文本包进`span leaf`，把图片`src`改为`data-src`，并规范化微信文章短链接。定位依靠可见文字、图片alt、相邻小标题与实际结构；不要假设文本节点后一定直接跟着br或图片一定在p里。读回标题图前后的元素再决定插入或替换位置。

文末留白采用独立`<p><br></p>`，配合约26px行高。连续两个br可能被编辑器重排，不能仅检查Markdown里有两个换行。两处加粗颜色为#406ADC，修改时也要检查内层span没有覆盖颜色。

更新请求的封面ID应使用上传回执中已知的有效`thumb_media_id`；云端稍后回读该字段可能为空而改为`thumb_url`，不能把空ID直接带入更新。本次实际遇到的40007就是需要检查这类字段的提示，不能靠重建重复草稿解决。

## 完成、重试与不确定结果

回读检查：原标题、作者、摘要、全文可见文字、图的数量与顺序、微信图床、固定文末、强调色、三处独立空白段落、指定链接及封面。微信规范化链接时保留原短链接文字，检查目标仍是微信文章规范链接；不要为此反复尝试绕过验证码。

40164白名单错误：报告接口本次返回的IP。用户说已添加后直接重试原授权动作。不要自动修改系统代理、切换其他账号或用被安全策略拒绝的浏览器接口规避。

创建请求超时且没有收到ID时，结果可能不确定。停止自动新建；先用允许的接口按标题及创建时段定位，或请用户在草稿箱确认，再把查到的ID绑定回执。工具标记`creation_outcome_unknown`时会阻止盲目重复创建。

回读失败但已有ID：保留ID，继续verify或更新该稿，不再新建。只有全部必要检查通过才报告保存完成。始终说明实际状态是草稿，不把保存说成发布。
