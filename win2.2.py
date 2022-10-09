import PySimpleGUI as psg

layout = [[psg.Text('Window 1')],
          [psg.Input(do_not_clear=True)],
          [psg.Text(size=(15,1), key='-OUTPUT-')],
          [psg.Button('Launch 2'), psg.Button('Exit')]]

win1 = psg.Window('Window 1', layout)

win2_active = False

while True:
    ev1, vals1 = win1.read(timeout=100)
    win1['-OUTPUT-'].update(vals1[0])
    if ev1 == psg.WIN_CLOSED or ev1 == 'Exit':
        break
    if not win2_active and ev1 == 'Launch 2':
        win2_active = True
        layout2 = [[psg.Text(key='-OUTPUT2-')],
                   [psg.Button('Exit')]]
        
        win2 = psg.Window('Window 2', layout2)
        
    if win2_active:
        ev2, vals2 = win2.read(timeout=100)
        win2['-OUTPUT2-'].update(vals1[0])
        if ev2 == psg.WIN_CLOSED or ev2 == 'Exit':
            win2_active = False
            win2.close()
            