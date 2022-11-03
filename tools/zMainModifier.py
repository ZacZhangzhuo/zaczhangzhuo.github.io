import os

#! ModificationPanel
IsModifyingTheArticles = False
IsDisplayItems = True
#! END modification panel

zWeArticleModifier = r'"tools\zWeArticleModifier.py"'
zAddItems = r'"tools\zAddItems.py"'
if IsModifyingTheArticles:
    os.system("python %s" % zWeArticleModifier)

if IsDisplayItems:
    os.system("python %s" % zAddItems)

# os.system(file1)
