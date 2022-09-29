import PySimpleGUI as psg
import os
from pathlib import Path

def add_files_in_folder(parent, dirname, recursion_limit, tree_created):
    if recursion_limit != 0:
        try:
            files = os.listdir(dirname)
        except PermissionError:
            return
        if not opened_folders.__contains__(dirname):
            opened_folders.append(dirname)
            for f in files:
                fullname = os.path.join(dirname, f)
                if os.path.isdir(fullname):  # if it's a folder, add folder and recurse
                    treedata.insert(parent, fullname, f, values=[], icon=folder_icon)
                    add_files_in_folder(fullname, fullname, recursion_limit - 1, tree_created)
                else:
                    treedata.insert(parent, fullname, f, values=[os.stat(fullname).st_size], icon=file_icon)

window = ('DIrmaker')                 

while True:  # Event Loop
    event, values = window.read()
    tree.update()
    try:
        v = values[tree_key][0]  # clicked file/folder
        print(v)
    except TypeError:
        pass
    if event == tree_key:
        add_files_in_folder(v, v, 2, False)
        tree.update(values=treedata) 

    if event in (sg.WIN_CLOSED, 'Cancel', True):
        break
    print(event, values)