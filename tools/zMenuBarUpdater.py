import os

MenuBarDir = [
    "zHome.html",
    "zDesigner\zDesigner.html",
    "zLearner\zLearner.html",
    "zWriter\zWriter.html",
    "zPhotographer\zPhotographer.html",
    "zIndividualDeveloper\zIndividualDeveloper.html",
    "zCV.html",
    "zSkills.html",
    "zContact.html",
]


allHtmlPaths = []

# Get all folder (only 3 layers)
# 1st sub folder
fileNames1 = os.listdir(".")
temp = []
for fileName in fileNames1:
    if os.path.isdir(fileName):
        temp.append(fileName)
fileNames1 = temp

# 2nd sub folder
fileNames2 = []
for fileName in fileNames1:
    temp = os.listdir(fileName)
    for t in temp:
        if os.path.isdir(fileName + "//" + t):
            fileNames2.append(fileName + "//" + t)

Paths = ["."]
Paths.extend(fileNames1)
Paths.extend(fileNames2)

# Get html folders
for Path in Paths:
    allHtmlPaths.extend([os.path.join(Path, i) for i in os.listdir(Path) if i[-5:] == ".html"])

# Operation
for htmlPath in allHtmlPaths:
    # Generating menu bar html
    barText = '<!-- Menu Bar --><div class="menuBar">'

    for MenuBar in MenuBarDir:
        barText = (
            barText
            + '<a href="'
            + os.path.relpath(MenuBar, htmlPath)[3:]
            + ' "class="menuBar"> <p>'
            + MenuBar.split("\\")[-1].replace(".html", "")
            + "</p></a>"
        )

    barText = barText + "</div><!-- End of Menu Bar -->"

    # Modifying the file
    html = open(htmlPath, "r", encoding="utf-8")
    htmlTexts = html.read()
    temp = htmlTexts.split("<!-- Menu Bar -->")
    
    if len(temp) == 2:
        temp1 = temp[0]
        temp2 = temp[1]
        temp3 = temp2.split("<!-- End of Menu Bar -->")[1]

        htmlTexts = temp1 + barText + temp3

        html = open(htmlPath, "w", encoding="utf-8")
        html.write(htmlTexts)
        print("z: MENU BAR OF THIS FILE HAS BEEN MODIFIED:" + htmlPath)
