import os

# import pyperclip
import datetime

#!Debug path
debugPath = r"C:\Zac\19 Github\ZacZhangzhuo.github.io\tools"
#!Modification path
modificationPath = r"C:\Zac\19 Github\ZacZhangzhuo.github.io"


def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t).replace(microsecond=0)


def compare_time(startTime, endTime, threshold="0000-00-00 00:10:00"):
    d_start = datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
    print(d_start)
    d_end = datetime.datetime.strptime(endTime, "%Y-%m-%d %H:%M:%S")
    threshold = datetime.datetime.strptime(threshold, "%Y-%m-%d %H:%M:%S")
    result =  d_start -  threshold
    return result


file_paths = []
current_address = os.path.dirname(debugPath)
for parent, dirnames, filenames in os.walk(current_address):
    # Case1: traversal the directories
    for dirname in dirnames:
        # print("Parent folder:", parent)
        file_paths.append(parent + "/" + dirname)
        # print("Dirname:", dirname)
        # file_paths.append()
    # Case2: traversal the files
    for filename in filenames:
        # print("Parent folder:", parent)
        file_paths.append(parent + "/" + filename)
        # print("Filename:", filename)
        # file_paths.append()

html_paths = []
html_times = []
for file_path in file_paths:
    if file_path.find(".html") != -1:
        html_paths.append(file_path)
        html_times.append(modification_date(file_path))

for html_time in html_times:
    print(compare_time(str(html_time), str(datetime.datetime.now().replace(microsecond=0)), "10"))


# print (html_paths)
