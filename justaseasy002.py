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


default_path = "e:/"

font = ('Courier New', 11)
sg.theme('SystemDefault')
sg.set_options(font=font)

DIR, FILE = True, False

data = {0: {'kind':DIR, 'path':'', 'file':'E:\\', 'children':None}, }
treedata = sg.TreeData()
treedata.insert('', 0, 'E:\\', [], icon=folder_icon)

layout = [
    [sg.Tree(treedata, headings=[], col0_width=30, num_rows=20, show_expanded=True, enable_events=True, key='-TREE-')],
    [sg.Text("",key='-folderrr-')],
    [sg.StatusBar("", size=(0, 1), key='-STATUS-')],
]

window = sg.Window("File Browser", layout, finalize=True, size=(1280,720))
tree = window['-TREE-']
tree.Widget.configure(show='tree')  # Hide header
tree.bind('<Double-1>', "DOUBLE-CLICK-")
tree.bind('<Button-1>', "SINGLE-CLICK-")
status = window['-STATUS-']


#print(status)
while True:

    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    status.update('')
    '''
    if event == '-TREE-SINGLE-CLICK-':
        print('Selected')
    '''
        
    if event == '-TREE-DOUBLE-CLICK-':
        #print('Double clicked...')
        parent_key = values['-TREE-'][0]
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
            tree.update(values=treedata)
            window['-folderrr-'].Update(path)
            #sg.Print(treedata)
            iid = tree.KeyToID[parent_key]
            tree.Widget.see(iid)

window.close()