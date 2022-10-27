import sys
import os
import PySimpleGUI as sg

sg.theme('SystemDefault')


"""
    Demo program that will display a folder hierarchy with icons for the folders and files.
    Note that if you are scanning a large folder then tkinter will eventually complain about too many bitmaps.
    This can be fixed easily enough by reusing the images within PySimpleGUI (enhancement request can be opened if you hit this problem)
"""

# Base64 versions of images of a folder and a file. PNG files (may not work with PySimpleGUI27, swap with GIFs)

folder_icon = 'icon/folder-50.png'
file_icon = 'icon/file-50.png'

starting_path = 'C:/Users'

if not starting_path:
    sys.exit(0)

treedata = sg.TreeData()


def add_files_in_folder(parent, dirname):
    files = os.listdir(dirname)
    for f in files:
        fullname = os.path.join(dirname, f)
        if os.path.isdir(fullname):            # if it's a folder, add folder and recurse
            treedata.Insert(parent, fullname, f, values=[], icon=folder_icon)
            add_files_in_folder(fullname, fullname)
        else:
            treedata.Insert(parent, fullname, f, values=[os.stat(fullname).st_size], icon=file_icon)

add_files_in_folder('', starting_path)

layout = [[sg.Text('File and folder browser Test')],
          [sg.Tree(data=treedata,
                   headings=['Size in kB', ],
                   auto_size_columns=True,
                   select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
                   num_rows=20,
                   col0_width=40,
                   key='-TREE-',
                   show_expanded=False,
                   enable_events=True,
                   expand_x=True,
                   expand_y=True,
                   ),],
          [sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('Tree Element Test', layout, resizable=True, finalize=True)

while True:     # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    print(event, values)
window.close()