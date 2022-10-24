import os
import datetime
# Modifying recent files function
def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t).replace(microsecond=0)

def IsOnTime(startTime, endTime, Minutes = 5):
    d_start = datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
    # print(d_start)
    d_end = datetime.datetime.strptime(endTime, "%Y-%m-%d %H:%M:%S")
    # thresholdInHour = datetime.datetime.strptime(thresholdInHour, "%Y-%m-%d %H:%M:%S")
    result = d_start + datetime.timedelta(minutes=Minutes) > d_end
    # print(result)
    return result

def ModifyRecentFile(IsModifyRecentFile, FolderPath, TimeIntervalMinutes = 5):
    if IsModifyRecentFile:
        file_paths = []
        current_address = os.path.dirname(FolderPath)
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

        changed_html_paths = []
        for t in range(len(html_times)):
            if IsOnTime(
                str(html_times[t]),
                str(datetime.datetime.now().replace(microsecond=0)),
                TimeIntervalMinutes,
            ):
                changed_html_paths.append(html_paths[t])

        for file in changed_html_paths:
            print("z: THIS FILE WOULD BE MODIFIED: " + file)

        return changed_html_paths
    else:
        return []



# END modifying recent files function