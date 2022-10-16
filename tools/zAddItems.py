"""
!Example
   <a href="2020-03-11 建筑思维与手机选择1/建筑思维与手机选择1.html">
        <img  class="items" src="2020-03-11 建筑思维与手机选择1/images/0001.jpg" alt="建筑思维与手机选择1">
      </a>
"""
import os
import sys
import copy

# ! Important params, always check before run
target = r"C:\Zac\19 Github\ZacZhangzhuo.github.io\zDesigner"
deleteTheFirstOne = True  # This tells if you wanna delete the html like zWriter
# !

fileNames = []
filePaths = []
images = []


for i, j, k in os.walk(target):
    fileNames.extend(k)
    filePaths.extend(j)
    images.extend(i)

# print(filePaths)
# print(fileNames)

# print(htmlNames)
if deleteTheFirstOne:
    fileNames = copy.deepcopy(fileNames[1:])
# print(htmlNames)

htmlNames = []
imageNames = []

for i in range(len(fileNames)):
    if fileNames[i].endswith("html"):
        htmlNames.append(fileNames[i])
        imageNames.append(fileNames[i+1])

outString = ""
for i in range(len(htmlNames) - 1, -1, -1):
    str1 = '<a href="'
    str2 = filePaths[i] + "/" + htmlNames[i]
    str3 = '">'
    str4 = '<img  class="items" src="'
    str5 = filePaths[i]
    str6 = '/images/'+imageNames[i]+'" alt="'
    str7 = htmlNames[i].split(".")[0]
    str8 = '"></a>'
    outString = outString + str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8

print(outString)
