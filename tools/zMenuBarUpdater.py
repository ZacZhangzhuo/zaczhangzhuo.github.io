import os
MenuBarDir = [
    "index.html",
    "zDesigner\zDesigner.html",
    "zLearner\zLearner.html",
    "zWriter\zWriter.html",
    "zPhotographer\zPhotographer.html",
    "zIndividualDeveloper\zIndividualDeveloper.html",
    "zCV.html",
    "zSkills.html",
    "zContact.html",
]

# p = "index.html"
# x= os.path.relpath(MenuBarDir[3], p)[3:]
# fileNames = []
# filePaths = []
# itemNames = []
# # Get all the files
# for i, j, k in os.walk("."):
#     filePaths.append(i)
#     fileNames.append(j)
#     itemNames.append(k)

# # Get all the html files and the location
# htmlPaths = []
# htmlNames = []
# for i in range(len(filePaths)):
#     if ''.join(itemNames).find(".html") != -1:
#         htmlPaths.append(filePaths[i])
#         htmlNames.append(itemNames[i])

# menuBar = """<!-- Menu Bar -->
#         <div class="menuBar">
#         <a href="../../zHome.html" class="menuBar"> <p>zHome</p></a>
#         <a href="../../zDesigner/zDesigner.html"class="menuBar"><p>zDesigner</p></a>
#         <a href="../../zLearner/zLearner.html"class="menuBar"><p>zLearner</p></a>
#         <a href="../../zWriter/zWriter.html"class="menuBar"><p>zWriter</p></a>
#         <a href="../../zPhotographer/zPhotographer.html"class="menuBar"><p>zPhotographer</p></a>
#         <a href="../../zIndividualDeveloper/zIndividualDeveloper.html"class="menuBar"><p>zIndividualDeveloper</p></a>
#         <a href="../../zCV.html" class="menuBar"><p>zCV</p></a>
#         <a href="../../zSkills.html" class="menuBar"><p>zSkills</p></a>
#         <a href="../../zContact.html" class="menuBar"><p>zContact</p></a>
#         </div>
#         <!-- End of Menu Bar -->"""
#     if file_path.find("zDesigner") != -1:
#         menuBar = menuBar.replace("/../zDesigner/", "/")
#     elif file_path.find("zLearner") != -1:
#         menuBar = menuBar.replace("/../zLearner/", "/")
#     elif file_path.find("zWriter") != -1:
#         menuBar = menuBar.replace("/../zWriter/", "/")
#     elif file_path.find("zPhotographer") != -1:
#         menuBar = menuBar.replace("/../zPhotographer/", "/")
#     elif file_path.find("zIndividualDeveloper") != -1:
#         menuBar = menuBar.replace("/../zIndividualDeveloper/", "/")
#     elif file_path.find("zCV") != -1:
#         menuBar = menuBar.replace("/../zCV/", "/")
#     elif file_path.find("zSkills") != -1:
#         menuBar = menuBar.replace("/../zSkills/", "/")
#     elif file_path.find("zContact") != -1:
#         menuBar = menuBar.replace("/../zContact/", "/")
#     else:
#         menuBar = menuBar.replace("../../z", "/z")
