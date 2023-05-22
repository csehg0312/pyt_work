import PySimpleGUI as psg

layout = [[psg.Text('Hello World')]]

window = psg.Window('Nice here', layout)

while True:
    event, val = window.read()
    if event == psg.WIN_CLOSED:
        break

window.close()