"""
!Example
   <a href="2020-03-11 建筑思维与手机选择1/建筑思维与手机选择1.html">
        <img  class="items" src="2020-03-11 建筑思维与手机选择1/images/0001.jpg" alt="建筑思维与手机选择1">
      </a>
"""

import sys
import os

sys.path.append("C:/Zac/GitHub")  # For Zorse
from Zorse import core_zHTML

target1 = r"zDesigner"
target2 = r"zIndividualDeveloper"
target3 = r"zLearner"
target4 = r"zWriter"
target5 = r"zPhotographer"
IsModifyRecentFile = True  # The html would be modified only when the subdirectory is changed.
deleteTheFirstOne = (
    True  # This tells if you wanna delete the html like zWriter - You always want to!
)
RecentMinutes = 5
targets = [target1, target2, target3, target4, target5]
# targets = [target1]

for target in targets:

    htmlNames = []
    imageNames = []

    fileNames = os.listdir(target)

    # Remove the first like zDesigner.html
    temp = []
    for fileName in fileNames:
        if os.path.isdir(target + '\\'+fileName):
            temp.append(fileName)
    fileNames = temp
    
    # Get the .html names
    for fileName in fileNames:
        temp = os.listdir(target+'\\'+fileName )
        
        for t in temp:
            if t.find(".html") != -1:
                htmlNames.append(t)
                break

    # Get the images
    for fileName in fileNames:
        imageNames.append(os.listdir(target + "//" + fileName + "//images")[0])

    # Modify recent files only
    isChange = False
    if IsModifyRecentFile:
        # Only  recent files
        for i in range(len(htmlNames)):
            htmlPath = target + "\\" + fileNames[i] + "\\" + htmlNames[i]
            if core_zHTML.IsRecentFile(htmlPath, RecentMinutes):
                isChange = True
    else:
        isChange = True


    # String
    if isChange:
        outString = "<!--! ADD NEW ARTICLE HERE -->"
        for i in range(len(htmlNames) - 1, -1, -1):
            str1 = '<a href="'
            str2 = fileNames[i] + "\\" + htmlNames[i]
            str3 = '">'
            str4 = '<img  class="items" src="'
            str5 = fileNames[i]
            str6 = "/images/" + imageNames[i] + '" alt="'
            str7 = fileNames[i].split(".")[0]
            str8 = '"></a>'
            outString = outString + str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8
        outString += "<!-- !End of Items -->"

        targetLocation = target + "\\" + target.split("\\")[-1] + ".html"
        html = open(targetLocation, "r", encoding="utf-8")
        htmlTexts = html.read()

        temp = htmlTexts.split("<!--! ADD NEW ARTICLE HERE -->")
        temp1 = temp[0]
        temp2 = temp[1]
        temp3 = temp2.split("<!-- !End of Items -->")[1]

        htmlTexts = temp1 + outString + temp3

        html = open(targetLocation, "w", encoding="utf-8")
        html.write(htmlTexts)
        print("z: THIS FILE WOULD BE MODIFIED:" + target.split("\\")[-1] + ".html")