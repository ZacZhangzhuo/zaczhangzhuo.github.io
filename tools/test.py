import os
import datetime

file_path = (
    r"C:\Zac\19 Github\ZacZhangzhuo.github.io\zCV.md"
)


def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)



print (modification_date(file_path))


