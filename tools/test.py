import re

file_path1 = r"C:\Zac\Github\ZacZhangzhuo.github.io\tools\t1.html"
file_path2 = r"C:\Zac\Github\ZacZhangzhuo.github.io\tools\t2.html"
# file_paths.extend(modificationPath)
# file_paths = ModifyRecentFile(IsModifyRecentFile, debugPath)


html1 = open(file_path1, "r", encoding="utf-8")
htmlTexts1 = html1.read()

html2 = open(file_path2, "r", encoding="utf-8")
htmlTexts2 = html2.read()

htmlTexts1 = re.sub("\s+", "", htmlTexts1).strip()
htmlTexts2 = re.sub("\s+", "", htmlTexts2).strip()

print(htmlTexts1 == htmlTexts2)
# print (htmlTexts1)
# print ('-----------------------------------------------------------------------------------------------------------------------')
# print (htmlTexts2)
