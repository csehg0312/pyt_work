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

window = psg.Window("Ablak", layout, size=(900,800), element_justification='l')

while True:
    event, values = window.read()
    '''
    if event == 'Submit':
        thisFile = values['-FILE_PATH-']
        with open(thisFile, 'r') as file:
            window['_multiline_'].Update(values[
                datao = file.read()
                encoded_bytes = datao.encode('utf-8', 'replace')
                dataod = encoded_bytes.decode('utf-8', 'replace')
                ])
            #datao = file.read()
            #encoded_bytes = datao.encode('utf-8', 'replace')
            #dataod = encoded_bytes.decode('utf-8', 'replace')
            #print(dataod)
            #window['_multiline_'].Update(values[])
        file.close()
        '''
    if event == 'SAVE':
        
        psg.Print('Saved')
        while values['-VER-'] == " ":
            print('not able to save')
            
        fvers = values['-VER-']
            
        
        #txtFile = values['-NAME-'] + fvers
        #print(txtFile)
        '''
        print(values['-NAME-'])
        with open(txtFile, 'w') as file:
            data = values['-NAME-']
            file.write(data)
        file.close()
        '''
        '''
        print(values['_multiline_'])
        
        with open(txtFile , 'w') as file:
            data = values['_multiline_']
            file.write(data)
        file.close()
        window['_saved_'].Update(visible=True)
        '''
    if event in (psg.WIN_CLOSED, 'EXIT'):
        break
        psg.Print('Exiting...')
    
window.close()
