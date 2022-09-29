import PySimpleGUI as psg
import os

layout = [[psg.Text('Egyszerű ablak')],[psg.Button('EXIT', size=(4,1))]]

window = psg.Window('Window', layout, size=(250,150))

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == 'EXIT':
        break
    
window.close()