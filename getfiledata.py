import os
import datetime

class File:
    def __init__(self, name, size, lastly_used):
        self.name = name
        self.size = size
        self.lastly_used = lastly_used
    
    def __str__(self):
        return f"{self.name} \nSize:{self.size} kB \nLastly used:{self.lastly_used}"
    

if __name__ == '__main__':
    filepath = input('Paste here file path: \n$')
    fsize = os.path.getsize(filepath)
    fsize = round(fsize / 1024, 2)
    finfo = os.stat(filepath)
    stats = os.stat(filepath)
    ftime = os.path.getmtime(filepath)
    unixToDatetime = datetime.datetime.fromtimestamp(ftime)
    #print(unixToDatetime)
    #print(fsize, 'kB')
    #print(finfo)
    #print(ftime)
    print(os.getlogin())
    project_file = File(filepath, fsize, unixToDatetime)
    print(project_file)