import PySimpleGUI as psg
from dataclass_utvonal import Jelen_EleresiUt
from dataclass_folder import Folder
import os
import shutil
mappa:str
mappa = ''
ut:str
ut = 'C:/Users/csehg/Documents'
szulo:str
szulo = 'C:/Users/csehg'

utvonal = Jelen_EleresiUt(szulo, mappa)
utvonal.UtvonalCsatlakozas()
print(os.getcwd())
psg.theme('LightYellow')

layout: list
layout = [[psg.Input(szulo,key='-IN-', enable_events=True)],
          [psg.Text('', key='-OUT-'), psg.Button('Refresh')],
          [psg.Listbox('', key='-LIST-', size=(25,20), change_submits=True, enable_events=True, sbar_background_color='#ffd700')]]

window = psg.Window('Jelenlegi Diszk',layout, grab_anywhere=True)

while True:
    event, values = window.read()
    window['-OUT-'].update(os.getcwd())
    
    if event == psg.WIN_CLOSED:
        break
    
    if (event == '-IN-') or (os.path.exists(values['-IN-']) == True):
        try:
            os.chdir(values['-IN-'])
            values['-OUT-'] = os.getcwd()
            if os.path.isdir(values['-IN-']) == True or os.path.ismount(values['-IN-']) == True:
                D: Folder
                search:str
                search = values['-IN-']
                D = Folder(search)
                lis:list = []
                lis = D.mappalista.default_factory.copy()
                #= D.mappalista.default_factory
                _ ,mappa = os.path.split(search) 
                new_values = [x for x in lis if mappa in x]
                print(new_values)
                #print(f'Folder has: {len(D.mappalista.default_factory)} entries')
                window['-LIST-'].Update(new_values)
        except OSError:
            continue
    
window.close()

