import PySimpleGUI as psg
import constandvar as cv
import os
import disk_detect01 as dd
import pathmanager as ph

def main_win():
    layoutv1 = [[psg.Text('This is a test layout'), psg.Text('Change the theme here:'), psg.Button('Theme', key='-THEME-')],
                [psg.Listbox([], size=(35,25), key='-LST1-', enable_events=True), psg.Listbox([], size=(35,25), key='-LST2-')],
                [psg.Ok(), psg.Button('Cancel')]
                ]
    windowv1 = psg.Window('This is next window', layoutv1, size=(700, 500))
    while True:
        event, values = windowv1.read(timeout=500)
        windowv1['-LST1-'].update(dd.drives)
        if event == '-LST1-':
            ph.path = values['-LST1-']
            length = len(ph.path)
            print(length)
            cv.BackPath = cv.BackPath.join(ph.path) + "/"
            lister = os.listdir(cv.BackPath)
            windowv1['-LST2-'].update(lister)
            
            
            
        if event in (psg.WIN_CLOSED, 'Cancel'):
            break
    windowv1.close()
    
