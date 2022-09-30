import PySimpleGUI as psg
import os

working_directory = os.getcwd()

layout = [[psg.Multiline(size=(120,35), tooltip='Ide irj', key='_multiline_')],
          [psg.Text('File Name '), psg.Input(size=(80, 10), key='-NAME-'), psg.Input('', key='-VER-')],
          [psg.Text('A fajl neve',key = '_savefile_', visible=True), psg.Input(size=(80, 10), key='-FILE_PATH-'),
           psg.FileBrowse(initial_folder=working_directory, font=('Times New Roman', 12), file_types = [('TXT Files','*.txt')]), psg.Button('Submit', font=('Times New Roman',12))],
          [psg.Text('Saved', key='_saved_', visible=False)],
          [psg.Button('SAVE', font=('Times New Roman', 12)), psg.Button('EXIT', font=('Times New Roman', 12)) ]
          ]

window = psg.Window('Ablak01', layout)

while True:
    event, values = window.read()
    
    if event == 'SAVE':
        window['_multiline_'].print('Saved')
        
    if event in (psg.WIN_CLOSED, 'EXIT'):
        break
    
window.close()