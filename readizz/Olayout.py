import PySimpleGUI as psg

layoutv1 = [[psg.Text('This is a test layout'), psg.Text('Change the theme here:'), psg.Button('Theme', key='-THEME-')],
            [psg.Listbox([], size=(35,25)), psg.Listbox([], size=(35,25))],
            [psg.Ok(), psg.Button('Cancel')]
            ]

windowv1 = psg.Window('This is next window', layoutv1, size=(700, 500))
