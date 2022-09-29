import PySimpleGUI as psg

layout = [[psg.Text('Egyszeri ablak')],
          [psg.InputText(key='-IN-')],
          [psg.Submit(), psg.Cancel()]]

window = psg.Window('Ablak', layout, size=(500,500))

event, values = window.read()

text_input=values['-IN-']

window.close()
psg.popup(text_input)
          