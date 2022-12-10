import os
import PySimpleGUI as psg
from pathlib import Path
from pathlib import PurePath
import table_functions as tf
import ddlistfunction as dd


ts_x = 750
ts_y = 25
path = 'C:/Users/csehg/Documents'
print(os.path.expanduser('~'))
tablework = os.listdir(path)
psg.theme('SystemDefault')

fejlec = ['Name', 'Size', 'Lastly Used', 'Extension']

vals = dd.calling(path)

infocenter = [[psg.Text('File:'), psg.Text('', enable_events=True, key='-FILENAME-')],
              [psg.Text('Size:'), psg.Text('', enable_events=True, key='-FILESIZE-')]
              ]


layout = [[ psg.Push(), psg.Image('iconexit.png', enable_events=True, pad=0, key='-EXIT-')],
          [psg.Table(vals,
                     headings=fejlec,
                     size=(ts_x,ts_y),
                     key='_T01_',
                     auto_size_columns=True,
                     enable_events=True), psg.Frame('', infocenter)],
          [psg.InputText(key='_IN_', size=(20,1)), psg.Button('Read')], [psg.Multiline('', key='_multiline_', size=(25,10), do_not_clear=True)]]

window = psg.Window(
    "Table",
    layout,
    size=(1280,720)
    )

while True:
    event, value = window.read()
    
    if event == '_T01_':
        kijelolt = [vals[row] for row in value[event]]
        print(kijelolt)
        window['-FILENAME-'].update(kijelolt[0][0])
        window['-FILESIZE-'].update(kijelolt[0][1])
    
    if event in (psg.WIN_CLOSED, '-EXIT-'):
        break
    
window.close()
