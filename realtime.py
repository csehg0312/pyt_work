import PySimpleGUI as psg

gui_rows = [[psg.Text("Hey", enable_events = True)],
            [psg.T(' ' * 10), psg.RealtimeButton('Forward')],
            [psg.RealtimeButton('Left'), psg.T(' ' * 15), psg.RealtimeButton('Right')],
            [psg.T(' ' * 10), psg.RealtimeButton('Reverse')],
            [psg.T('')],
            [psg.Quit(button_color = ('black', 'orange'))]
            ]

window = psg.Window('hey not me', gui_rows)

while True:
    event, values = window.read(timeout=50)
    print(event)
    if event in ('Quit', psg.WIN_CLOSED):
        break

window.close()