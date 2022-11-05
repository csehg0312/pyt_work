import os
 
# This is my path
path = "/storage/emulated"
 
# Scan the directory and get
# an iterator of os.DirEntry objects
# corresponding to entries in it
# using os.scandir() method


try:
    obj = os.scandir(path)
    print("Files and Directories in '% s':" % path)
    for entry in obj:
        if entry.is_dir() or entry.is_file():
        	print(entry.name)
except:
	print('Permission denied')