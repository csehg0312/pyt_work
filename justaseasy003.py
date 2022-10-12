from pathlib import Path
import PySimpleGUI as sg

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
treedata = sg.TreeData()
treedata.insert('', 0, 'C:\\', [], icon=folder_icon)

layout = [
    [sg.Tree(treedata, headings=[], col0_width=30, num_rows=20, show_expanded=True, enable_events=True, key='-TREE01-'),sg.Tree(treedata, headings=[], col0_width=30, num_rows=20, show_expanded=True, enable_events=True, key='-TREE02-')],
    [sg.Text("",key='-folderrr01-'),sg.Text("", key='-folderrr02-')],
    [sg.StatusBar("", size=(0, 1), key='-STATUS-')],
]

window = sg.Window("File Browser", layout, finalize=True, size=(1280,720))
tree01 = window['-TREE01-']
tree01.Widget.configure(show='tree')  # Hide header
tree01.bind('<Double-1>', "DOUBLE-CLICK-")
tree02 = window['-TREE02-']
tree02.Widget.configure(show='tree')
tree02.bind('<Double-1>', "DOUBLE-CLICK-")
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
                #print(data[key])
            tree01.update(values=treedata)
            window['-folderrr01-'].Update(path)
            #sg.Print(treedata)
            iid = tree01.KeyToID[parent_key]
            tree01.Widget.see(iid)
            
    if event == '-TREE02-DOUBLE-CLICK':
        print("Double clicked")
        parent_key = values['-TREE02-'][0]
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
                #print(data[key])
            tree02.update(values=treedata)
            window['-folderrr02-'].Update(path)
            #sg.Print(treedata)
            iid = tree02.KeyToID[parent_key]
            tree02.Widget.see(iid)
        

window.close()