import os

#! ModificationPanel
IsAddingItemsInTheMenu = True
IsChangingTheCV = True
#! END modification panel

zAddItems = r'"tools\zAddItems.py"'
zCVToHtml = r'tools\zCVToHtml.py'

if IsAddingItemsInTheMenu:
    os.system("python %s" % zAddItems)
    
if IsChangingTheCV:
    os.system("python %s" % zCVToHtml)

