from pathlib import Path
import pathlib
import PySimpleGUI as sg
import os
import datetime

class File:
    def __init__(self, name, size, size_in, lastly_used):
        self.name = name
        self.size = size
        self.size_in = size_in
        self.lastly_used = lastly_used
    
    def __str__(self):
        return f"{self.name} \nSize:{self.size} {self.size_in} \nLastly used:{self.lastly_used}"
    


#nows = dt.now()

def new_key():
    key = 1
    while key in data:
        key += 1
    return key

folder_icon = 'icon/folder-50.png'
file_icon = 'icon/file-50.png'


deafult_path = "c:/"

font = ('Courier New', 11)
sg.theme('SystemDefault')
sg.set_options(font=font)

DIR, FILE = True, False

data = {0: {'kind':DIR, 'path':'', 'file':'C:\\', 'children':None}, }
Fdata = {0: {'path':'', 'file':'C:\\'}, }
phile_data = 'C://'
treedata = sg.TreeData()
treedata.insert('', 0, 'C:\\', [], icon=folder_icon)

layout = [
    [sg.Tree(treedata, headings=[], col0_width=30, num_rows=20, show_expanded=True, enable_events=True, key='-TREE01-'),
     sg.Multiline(size=(35,20), enable_events=True, key='_multiline_', do_not_clear=False)],
    [sg.Text("",key='-folderrr01-'),sg.Text("", key='-folderrr02-')],
    [sg.StatusBar("", size=(0, 1), key='-STATUS-')],
]

window = sg.Window("File Browser", layout, finalize=True, size=(1280,720))
tree01 = window['-TREE01-']
tree01.Widget.configure(show='tree')  # Hide header
tree01.bind('<Double-1>', "DOUBLE-CLICK-")
status = window['-STATUS-']


#print(status)
'''
FIXME: In the first treeview is possible to open with -DOUBLE-CLICK-, but in the second treeview is not WHY is that?
'''
while True:

    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    status.update('')
    if event == '-TREE01-DOUBLE-CLICK-':
        #print('Double clicked...')
        parent_key = values['-TREE01-'][0]
        #print(parent_key)
        node = data[parent_key]
        #window('-folderrr-').Update(values['node'])
        #print(node)
        if node['kind'] == DIR and node['children'] == None:
            parent_path = Path(node['path']).joinpath(node['file'])
            #print(parent_path)
            
            try:
                files = sorted(list(parent_path.iterdir()), key=lambda file:file.is_file())
                #print(files)
            except:
                status.update("Access is denied")
                continue
            node['children'] = []
            for item in files:
                key = new_key()
                #print(key)
                kind, path, file = item.is_dir(), str(item.parent), item.name
                #print(kind)
                #print(path)
                #window['-folderrr-'].Update(path)
                #print(file)
                #print("---")
                treedata.insert(parent_key, key, str(file), [], icon=folder_icon if kind == DIR else file_icon)
                node['children'].append(key)
                data[key] = {'kind':kind, 'path':path, 'file':file, 'children':None}
                #print(file)
                #print(data[key])
            tree01.update(values=treedata)
            window['-folderrr01-'].Update(path)
            #sg.Print(treedata)
            iid = tree01.KeyToID[parent_key]
            tree01.Widget.see(iid)
        else:
            phile_key = values['-TREE01-'][0]
            phile_node = data[phile_key]
            
            keys = []
            Vvalues = []
            #items = phile_node.items()
            
            Fpath = '' 
            for i in phile_node:
                #print(i)
                nkey = i
                if nkey == 'path':
                    print('its that')
                    #print(phile_node[i])
                    Fpath = phile_node[i]
                    print(Fpath)
                elif nkey == 'file':
                    #print(phile_node[i])
                    Fname = phile_node[i]
                    Fpath = Fpath + '/' + phile_node[i]
                    print(Fpath)
            fsize = os.path.getsize(Fpath)
            fsize = round(fsize / 1024, 2)
            #itssize = 'kB'
            if fsize >= 1024:
                fsize = round(fsize / 1024, 2)
                itssize = 'MB'
            else:
                itssize = 'kB'
        
            finfo = os.stat(Fpath)
            stats = os.stat(Fpath)
            ftime = os.path.getmtime(Fpath)
            unixToDatetime = datetime.datetime.fromtimestamp(ftime)
            current_file = File(Fname, fsize, itssize, unixToDatetime)
            window['_multiline_'].print(current_file)

window.close()