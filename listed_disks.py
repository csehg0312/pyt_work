import PySimpleGUI as psg
import os
import os.path
import disk
import disk_detect01 as ds

path = " "
queue = []

layout = [
    [psg.Text('Drive detector')],
    [psg.Listbox([], key='_Olist_', size=(30,25), enable_events=True)]
    ]

window = psg.Window('Detector', layout)

#print(disk.total)

while True:
    event, values = window.read(timeout=500)
    if event == psg.WIN_CLOSED:
        break
    window['_Olist_'].update(ds.drives)
    unckeckeddrives = ['%s:' % d for d in ds.dl if os.path.exists('%s:' % d)]
    x = ds.diff(unckeckeddrives, ds.drives)
    if x:
        ds.det()
    x = ds.diff(ds.drives, unckeckeddrives)
    if x:
        ds.rem()
    ds.drives = ['%s:' % d for d in ds.dl if os.path.exists('%s:' % d)]
    if event == '_Olist_':
        curr = values['_Olist_']
        currSO = ""
        currS = currSO.join(curr)
        #path = path + "/" + currS
        #dir_list = os.listdir(path)
        queue.append(currS)
        print(queue)
    
window.close()    