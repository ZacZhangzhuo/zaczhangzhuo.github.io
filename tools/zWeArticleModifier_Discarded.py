

from zRecentFileModification import ModifyRecentFile


#!PATH
IsModifyRecentFile = False
#!Debug path
debugPath = r"C:\Zac\Github\ZacZhangzhuo.github.io\tools"
#!Modification folder path
modificationPath = r"C:\Zac\Github\ZacZhangzhuo.github.io"
#! END file path


file_paths = modificationPath
file_paths = ModifyRecentFile(IsModifyRecentFile, debugPath)

for file_path in file_paths:

    html = open(file_path, "r", encoding="utf-8")
    htmlTexts = html.read()

    # Add Menu Bar
    menuBar = """<!-- Menu Bar -->
        <div class="menuBar">
        <a href="../../zHome.html" class="menuBar"> <p>zHome</p></a>
        <a href="../../zDesigner/zDesigner.html" class="menuBar"><p>zDesigner</p></a>
        <a href="../../zLearner/zLearner.html" class="menuBar"><p>zLearner</p></a>
        <a href="../../zWriter/zWriter.html" class="menuBar"><p>zWriter</p></a>
        <a href="../../zPhotographer/zPhotographer.html" class="menuBar"><p>zPhotographer</p></a>
        <a href="../../zDeveloper/zDeveloper.html" class="menuBar"><p>zDeveloper</p></a>
        <a href="../../zCV.html" class="menuBar"><p>zCV</p></a>
        <a href="../../zSkills.html" class="menuBar"><p>zSkills</p></a>
        <a href="../../zContact.html" class="menuBar"><p>zContact</p></a>
        </div>
        <!-- End of Menu Bar -->"""
    if file_path.find("zDesigner") != -1:
        menuBar = menuBar.replace("/../zDesigner/", "/")
    elif file_path.find("zLearner") != -1:
        menuBar = menuBar.replace("/../zLearner/", "/")
    elif file_path.find("zWriter") != -1:
        menuBar = menuBar.replace("/../zWriter/", "/")
    elif file_path.find("zPhotographer") != -1:
        menuBar = menuBar.replace("/../zPhotographer/", "/")
    elif file_path.find("zDeveloper") != -1:
        menuBar = menuBar.replace("/../zDeveloper/", "/")
    elif file_path.find("zCV") != -1:
        menuBar = menuBar.replace("/../zCV/", "/")
    elif file_path.find("zSkills") != -1:
        menuBar = menuBar.replace("/../zSkills/", "/")
    elif file_path.find("zContact") != -1:
        menuBar = menuBar.replace("/../zContact/", "/")
    else:
        menuBar = menuBar.replace("../../z", "/z")

    htmlTexts = htmlTexts.replace("<body class='appmsg_skin_default'>", "<body>" + menuBar)
    htmlTexts = htmlTexts.replace('<body class="vscode-body vscode-light">', "<body>" + menuBar)
    htmlTexts = htmlTexts.replace('<body for="html-export">', "<body>" + menuBar)

    # Replace the comment
    htmlTexts = htmlTexts.replace("提供的爬取软件来源于：i.ijrou.com 免费下载使用", "Designer by ArchZ")

    # Replace the style sheet link
    htmlTexts = htmlTexts.split("<style>")
    if len(htmlTexts) != 1:
        tempTexts = htmlTexts[-1].split("</style>")[-1]
        htmlTexts = (
            htmlTexts[0] + '<link rel="stylesheet" href="../../zMarkdownStyles.css" />' + tempTexts
        )
    else:
        htmlTexts = htmlTexts[0]

    # Replace the styles
    splittedTexts = htmlTexts.split('style="')
    htmlTexts = splittedTexts[0]
    for i in splittedTexts[1:]:
        if i.find("text-align: center") == -1:
            htmlTexts = htmlTexts + i.split('"', 1)[1]
        else:
            htmlTexts = htmlTexts + 'style="text-align: center;"' + i.split('"', 1)[1]

    # Replace read the article
    htmlTexts = htmlTexts.replace("阅读原文", " ")

    # Replace user comments
    beReplaced = """
    用户设置不下载评论
    """
    htmlTexts = htmlTexts.replace(beReplaced, " ")

    beReplaced = """
    精选留言
    """
    htmlTexts = htmlTexts.replace(beReplaced, " ")

    beReplaced = '<p class="endnotes">--- Growing, Growing, Brighter Everyday ! ---</p>'
    htmlTexts = htmlTexts.replace(beReplaced, " ")

    beReplaced = "</body>"
    htmlTexts = htmlTexts.replace(
        beReplaced, '<p class="endnotes">--- Growing, Growing, Brighter Everyday ! ---</p></body>'
    )

    html = open(file_path, "w", encoding="utf-8")
    # print (index)
    # print(htmlTexts)
    # pc.copy(htmlTexts)
    html.write(htmlTexts)
