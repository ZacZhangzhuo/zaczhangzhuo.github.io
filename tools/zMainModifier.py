import os

#! ModificationPanel
IsModifyingTheArticles = True
IsDisplayItems = True
#! END modification panel

zWeArticleModifier = r'"C:\Zac\19 Github\ZacZhangzhuo.github.io\tools\zWeArticleModifier.py"'
zAddItems = r'"C:\Zac\19 Github\ZacZhangzhuo.github.io\tools\zAddItems.py"'
if IsModifyingTheArticles:
    os.system("python %s" % zWeArticleModifier)

if IsDisplayItems:
    os.system("python %s" % zAddItems)

# os.system(file1)
