import PySimpleGUI as psg
import datetime 
import os

working_directory = os.getcwd()

#todo Realize how to use menu buttons and link to them functions when pressed
#todo Make a function that is linked to open menu button
#todo Make function with what its possible to open txt files and then save them
#todo A functoin to open a file
#todo A function to save a file and close a file
#todo Make function with that it is possible to save files to a specific location

def getTime():
    return datetime.datetime.now().strftime('%p %I:%M:%S')

def make_window(theme):
    psg.theme(theme)
    layout = [	#[psg.Menu(menu_def, background_color='lightsteelblue',text_color='navy', disabled_text_color='yellow', font='Verdana', pad=(10,10))],
        [psg.ButtonMenu('', [['nf', 'op','om','---','rf','cl'],['New File', 'Open','Open Module','---','Recent Files','Close']],image_filename ='icon/plus-50.png',border_width=1, background_color='gray',),psg.ButtonMenu('', [['rm', 'rc','sm','ps'],['Run', 'Run Module','Shell','Python module']],image_filename ='icon/cut-50.png', border_width=1, background_color='gray'),psg.ButtonMenu('Terminate', [['ex', 'cl','---','ab'],['Exit', 'Close','---','About us...']], border_width=1, background_color='gray'), psg.Text('', size=(20,2), key='_clock_', justification='right')],
        [psg.Multiline(size=(120,25),tooltip='Write your Text here', key='_multiline_')],
        [psg.Text('File Name'),psg.Input(key='_openfile_'),psg.OptionMenu(values=['.txt','.pdf', '.dat','.sql', '.doc', '.py', '.html', '.js', '.css'],size=(4,8),default_value='.doc',key='ftype')],
        [psg.Text('A fajl neve',key = '_savefile_', visible=True), psg.Input(size=(80, 10), key='-FILE_PATH-'),
         psg.FileBrowse(initial_folder=working_directory, font=('Times New Roman', 12), file_types = [('All Files','*.*')]), psg.Button('Submit', font=('Times New Roman',12))],
        [psg.Text('Saved', key='_saved_', visible=False)],
        [psg.Button('SAVE', font=('Times New Roman',12)),psg.Button('CANCEL', font=('Times New Roman',12))],
        [psg.Text('Kerlek valassz egy temat: '), psg.Combo(psg.theme_list(), default_value=theme, enable_events=True, key='-THEMES-')],]
    
    return psg.Window('Fajlszerkeszto', layout, finalize=True)



def main():
    window = make_window('Reddit')
    while True:
        event, values = window.read()
        print(event)
        if event == 'Submit':
            thisFile = values['-FILE_PATH-']
            with open(thisFile, 'r') as file:
                datao = file.read()
                encoded_bytes = datao.encode('utf-8', 'replace')
                dataod = encoded_bytes.decode('utf-8', 'replace')
                #print(datao)
                values['_multiline_'] = dataod
            file.close()
            
            
        if event == 'SAVE':
            
            theFile = values['_openfile_'] + values['ftype']
            print(theFile)
      
            #print(values['_multiline_'])
            
            with open(theFile , 'w') as file:
                data = values['_multiline_']
                file.write(data)
            file.close()
            window['_saved_'].Update(visible=True)
            
            file.close();
            
        if event == psg.WINDOW_CLOSED or event == 'CANCEL':
            break
        window.find_element('_clock_').Update(getTime())
        if values['-THEMES-']:
            window.close()
            window = make_window(values['-THEMES-'])
            
    window.close()    
     
if __name__ == '__main__':
    main()
