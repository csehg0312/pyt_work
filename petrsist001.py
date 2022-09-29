import PySimpleGUI as psg

layout = [[psg.Text('Persistent window')], [psg.Input()], [psg.Button('Read'), psg.Exit()]]

window = psg.Window('Window that stays open', layout, grab_anywhere=False)

while True:
        event, values = window.read()
        print (event, values)
        if event in (psg.WIN_CLOSED, 'Exit'):
            break
        
window.close()