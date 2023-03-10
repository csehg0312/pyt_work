import PySimpleGUI as psg
from dataclass_utvonal import Jelen_EleresiUt
from dataclass_file import File
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
        if os.path.isdir(values['-IN-']):
            
            os.chdir(values['-IN-'])
            values['-OUT-'] = os.getcwd()
        if os.path.isdir(values['-IN-']) == False and os.path.isfile(values['-IN-']) == True:
            F: File
            P, fl = os.path.split(values['-IN-'])
            F = File(P, fl)
            print(f'Filename is: {F.nev.default_factory} and extension is: {F.bovitmeny.default_factory}')
            print(f'Modified: {F.modositdate.default_factory}')
            print(f'Size: {F.meret.default_factory}')
   
    
window.close()

