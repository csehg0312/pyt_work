import os
import PySimpleGUI as psg
import table_work as tw
import table as tb
 
# Get the list of all files and directories
 
#print("Files and directories in '", path, "' :")
ts_x = 150
ts_y = 25
path = "C:/"
tablework = os.listdir(path)

fejlec = ['Name']

vals = [[tablework[i] for j in range(1)] for i in range(len(tablework))]

layout = [[psg.Table(vals, headings=fejlec, size=(ts_x,ts_y), key='_T01_', auto_size_columns=False, enable_events=True)],
          [psg.InputText(key='_IN_', size=(20,1)), psg.Button('Read')], [psg.Multiline('', key='_multiline_', size=(25,10), do_not_clear=True)]]

window = psg.Window("Table", layout, size=(750,500))

while True:
    event, value = window.read()
    
    if event == '_T01_':
        data_str = ""
        data_str01 = ""
        print('table1')
        data_selected = [vals[row] for row in value[event]]
        data_selected = [map(str,l) for l in data_selected]
        for l in data_selected:
            pathnext = path + path.join(l)
        print(pathnext)
    
    if event == psg.WIN_CLOSED:
        break
    
window.close()