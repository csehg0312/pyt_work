import PySimpleGUI as psg
print("PSG imported...")
import os
print("OS imported...")

working_directory = os.getcwd()
print("working_directory is ", working_directory)
psg.theme('Reddit')
tema = psg.theme()
print('the theme is', tema)

layout = [[psg.Multiline(size=(120,35), tooltip='Ide irj', key='_multiline_', do_not_clear=False)],
          [psg.Text('File Name '), psg.Input(size=(80, 10), key='-NAME-'), psg.Input('', key='-VER-')],
          [psg.Text('A fajl neve',key = '_savefile_', visible=True), psg.Input(size=(80, 10), key='-FILE_PATH-'),
           psg.FileBrowse(initial_folder=working_directory, font=('Times New Roman', 12), file_types = [('ALL Files','*.* *')]), psg.Button('Submit', font=('Times New Roman',12))],
          [psg.Text('Saved', key='_saved_', visible=False)],
          [psg.Button('SAVE', font=('Times New Roman', 12)), psg.Button('EXIT', font=('Times New Roman', 12)) ]
          ]
#print(layout)

window = psg.Window("Ablak", layout, size=(900,800), element_justification='l')
print(window)
multiline = psg.Multiline()

while True:
    event, values = window.read()
    
    if event == 'Submit':
        window['_multiline_'].print(" ")
        thisFile = values['-FILE_PATH-']
        with open(thisFile, 'r') as file:
            datao = file.read()
            #encoded_bytes = datao.encode('utf-8', 'replace')
            #datao_dec = datao.decode('utf-8', 'replace')
            window['_multiline_'].print(datao)
               
        file.close()
        
    if event == 'SAVE':
        
        #psg.Print('Saved')
        multiline.print(" ")
        multiline.print("Saved")
            
        
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
        print('Exiting...')
        break
    
window.close()
