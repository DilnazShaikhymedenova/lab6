# 3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

import os

path = r"C:\Users\alser\Downloads"  #Downloads is a directory that contains files and possibly other directories.

if os.path.exists(path):
    print("Path exists")
    directory, filename = os.path.split(path)
    print("Directory:", directory)
    print("Filename:", filename)
else:
     print("Path does not exist")