"""
ArchZ file naming rule:
- Use hump nomenclature rule (eg. 'zDesign') for file names, code variables, compunctions tec.
- Avoid using space in any name.
- Create a folder for each article. The name of the folder can be different from the .html file. the .html which is a sub-item of the file. 
- Possible to add multiple items in the main folder of the article, but only one .html can exist.
- Possible to create as many sub-files as you wish under the folder of the article for storing resources.
- Under the folder of the article, a 'image' file most be created, and the first image of the file will be the profile of the article in the menu.
- Bar updater only read the first three layers of the files
"""


import os

#! ModificationPanel
IsAddingItemsInTheMenu = True
IsChangingTheCV = True
#! END modification panel

zAddItems = r'"tools\zAddItems.py"'
zCVToHtml = r"tools\zCVToHtml.py"

if IsAddingItemsInTheMenu:
    os.system("python %s" % zAddItems)

if IsChangingTheCV:
    os.system("python %s" % zCVToHtml)
