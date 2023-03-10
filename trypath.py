import PySimpleGUI as psg
from dataclass_utvonal import Jelen_EleresiUt
from dataclass_drive import Drive
import os
import shutil
mappa:str
mappa = 'Documents'
ut:str
ut = 'C:/Users/csehg/Documents'
szulo:str
szulo = 'C:/Users/csehg'

utvonal = Jelen_EleresiUt(szulo, mappa)
utvonal.UtvonalCsatlakozas()
print(os.getcwd())

layout: list
layout = [[psg.Input('',key='-IN-')],
          [psg.Text('', key='-OUT-'), psg.Button('Refresh')]]

window = psg.Window('Jelenlegi Diszk',layout)

while True:
    event, values = window.read(timeout=50)
    window['-OUT-'].update(os.getcwd())
    
    if event == psg.WIN_CLOSED:
        break
    
    if (event == '-IN-') or (os.path.exists(values['-IN-']) == True):
        try:
            os.chdir(values['-IN-'])
            values['-OUT-'] = os.getcwd()
            if os.path.ismount(values['-IN-']):
                teljes, foglalt, szabad = shutil.disk_usage(values['-IN-'])
                D: Drive
                D = Drive(values['-IN-'], teljes, foglalt, szabad)
                
                print(f'Foglalt: {D.Foglalt.default_factory}')
        except TypeError:
            continue
    
window.close()
