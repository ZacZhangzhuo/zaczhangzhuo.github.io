import pyperclip as pc

file_path = (
    r"C:\Zac\19 Github\ZacZhangzhuo.github.io\zDesigner\2022-05-01 Section Clipper —— 课程设计\Section Clipper —— 课程设计.html"
)

html = open(file_path, "r", encoding="utf-8")
htmlTexts = html.read()


htmlTexts = htmlTexts.split("<style>")
tempTexts = htmlTexts[-1].split("</style>")[-1]

htmlTexts = htmlTexts[0] + '<link rel="stylesheet" href="../../zMarkdownStyles.css" />' + tempTexts

# Replace the comment
htmlTexts = htmlTexts.replace("提供的爬取软件来源于：i.ijrou.com 免费下载使用", "Designer by ArchZ")


#Replace the styles
splittedTexts = htmlTexts.split('style="')
htmlTexts = splittedTexts[0]
for i in splittedTexts[1:]:
    if ( i.find('text-align: center') == -1):
        htmlTexts = htmlTexts + i.split('"', 1)[1]
    else:
        htmlTexts = htmlTexts + 'style="text-align: center;"' + i.split('"', 1)[1]
    
    
# Replace user comments
beReplaced = """<div class="comment">
				<h3 style="margin:26px 0;font-weight:100;padding-bottom:4px;border-bottom:1px solid #ccc;">精选留言</h3>
				用户设置不下载评论
			</div>"""
htmlTexts = htmlTexts.replace(
    beReplaced, '<p class="endnotes">--- Growing, Growing, Brighter Everyday ! ---</p>'
)

beReplaced = """<div class="comment">
				<h3 >精选留言</h3>
				用户设置不下载评论
			</div>"""
htmlTexts = htmlTexts.replace(
    beReplaced, '<p class="endnotes">--- Growing, Growing, Brighter Everyday ! ---</p>'
)

html = open(file_path, "w", encoding="utf-8")
# print (index)
# print(htmlTexts)
# pc.copy(htmlTexts)
html.write(htmlTexts)
