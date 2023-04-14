import PySimpleGUI as psg
from search_try03 import binaris_atvitel
import os
vals:list = os.listdir(os.getcwd())

layout = [[psg.Text('Search Engine')],
          [psg.Input(os.getcwd(), key="PATH"), psg.Button('Utvonal')],
          [psg.Input('',key='-SEARCH-'), psg.Button('Kereses')],
          [psg.Listbox(vals,key="-DATASET-", size=(75,35))]
          ]

window = psg.Window('Search engine', layout, size=(600,600))

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    if event == 'Kereses':
        window['-DATASET-'].update(binaris_atvitel(sorted(os.listdir(os.getcwd())), values['-SEARCH-']))
        print(values['-SEARCH-'])
#         print(binaris_kereses(sorted(vals), values['-SEARCH-']))
    if event == 'Utvonal' and os.path.exists(values['PATH']) == True and os.path.isdir(values['PATH']) == True:
        os.chdir(values['PATH'])
        window['-DATASET-'].update(os.listdir(os.getcwd()))
        
    
window.close()
    
