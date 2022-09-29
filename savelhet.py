import PySimpleGUI as psg
import os

working_directory = os.getcwd()

layout = [[psg.Multiline(size=(80,10), tooltip='Ide irj', key='_multiline_')],
          [psg.Input(size=(80, 10), key='-NAME-')],
          [psg.Button('PASTE')],
          [psg.Text('Saved', key='_saved_', visible=False)],
          [psg.Button('SAVE', font=('Times New Roman', 12)), psg.Button('EXIT', font=('Times New Roman', 12)) ]
          ]

window = psg.Window("Ablak", layout)

while True:
    event, values = window.read()
    if event == 'SAVE':
        '''
        print(values['-NAME-'])
        with open('output.txt', 'w') as file:
            data = values['-NAME-']
            file.write(data)
        file.close()
        '''
        print(values['_multiline_'])
        with open('output.txt', 'w') as file:
            data = values['_multiline_']
            file.write(data)
        file.close()
        window['_saved_'].Update(visible=True)
    if event == 'PASTE':
        print(values['_multiline_'])
        dataod = values['_multiline_']
        window('-NAME-').Update(values[dataod])
    
    if event in (psg.WIN_CLOSED, 'EXIT'):
        break
    
window.close()