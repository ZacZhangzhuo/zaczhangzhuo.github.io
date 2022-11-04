"""
!Example
   <a href="2020-03-11 建筑思维与手机选择1/建筑思维与手机选择1.html">
        <img  class="items" src="2020-03-11 建筑思维与手机选择1/images/0001.jpg" alt="建筑思维与手机选择1">
      </a>
"""
import os
import sys
import copy
from zRecentFileModification import IsOnTime
from zRecentFileModification import modification_date
import datetime


# IsModifyRecentFile = True - Discard
# target0 = r"C:\Zac\GitHub\ZacZhangzhuo.github.io\tools"
target1 = r"C:\Zac\Github\ZacZhangzhuo.github.io\zDesigner"
target2 = r"C:\Zac\Github\ZacZhangzhuo.github.io\zIndividualDeveloper"
target3 = r"C:\Zac\Github\ZacZhangzhuo.github.io\zLearner"
target4 = r"C:\Zac\Github\ZacZhangzhuo.github.io\zWriter"
target5 = r"C:\Zac\Github\ZacZhangzhuo.github.io\zPhotographer"
deleteTheFirstOne = (
    True  # This tells if you wanna delete the html like zWriter - You always want to!
)
targets = [target1, target2,target3, target4,target5]

for target in targets:
    fileNames = []
    filePaths = []
    images = []

    # Get all the files
    for i, j, k in os.walk(target):
        fileNames.extend(k)
        filePaths.extend(j)
        images.extend(i)

    # This tells if you wanna delete the html like zWriter
    if deleteTheFirstOne:
        fileNames = copy.deepcopy(fileNames[1:])

    # Only keep .html files and the first image
    htmlNames = []
    imageNames = []
    for i in range(len(fileNames)):
        if fileNames[i].endswith("html"):
            htmlNames.append(fileNames[i])
            for j in range(i, len(fileNames)):
                if fileNames[j].endswith('jpg') or fileNames[j].endswith('png') or fileNames[j].endswith('jpeg'):
                    imageNames.append(fileNames[j])
                    break
            
    # print (imageNames)

    #  Discard -------------------------------
    # # Only keep recent files
    # tempHtmlNames =[]
    # tempImageNames = []
    # for i in range(len(htmlNames)):
    #     if IsOnTime(
    #             str(modification_date(target + '\\'+filePaths[i]+'\\'+ htmlNames[i])),
    #             str(datetime.datetime.now().replace(microsecond=0)),
    #     ):
    #         tempHtmlNames.append(htmlNames[i])
    #         tempImageNames.append(imageNames[i])
    # htmlNames = tempHtmlNames
    # imageNames = tempImageNames
    #  Discard -------------------------------

    outString = "<!--! ADD NEW ARTICLE HERE -->"
    for i in range(len(htmlNames) - 1, -1, -1):
        str1 = '<a href="'
        str2 = filePaths[i] + "/" + htmlNames[i]
        str3 = '">'
        str4 = '<img  class="items" src="'
        str5 = filePaths[i]
        str6 = "/images/" + imageNames[i] + '" alt="'
        str7 = htmlNames[i].split(".")[0]
        str8 = '"></a>'
        outString = outString + str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8
    outString += "<!-- !End of Items -->"

    file_path = target + "\\" + target.split("\\")[-1] + ".html"
    html = open(file_path, "r", encoding="utf-8")
    htmlTexts = html.read()
    
    temp1 = htmlTexts.split("<!--! ADD NEW ARTICLE HERE -->")[0]
    temp2 = htmlTexts.split("<!--! ADD NEW ARTICLE HERE -->")[1]
    temp3 = temp2.split("<!-- !End of Items -->")[1]

    htmlTexts = temp1 + outString + temp3
    
    
    html = open(file_path, "w", encoding="utf-8")
    html.write(htmlTexts)
    # print (htmlTexts)
    print("z: THIS FILE WOULD BE MODIFIED:" + target.split("\\")[-1] + ".html")
