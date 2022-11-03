import os

#! ModificationPanel
IsAddingItemsInTheMenu = True
#! END modification panel

zAddItems = r'"tools\zAddItems.py"'

if IsAddingItemsInTheMenu:
    os.system("python %s" % zAddItems)

