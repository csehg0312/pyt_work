import os
import sys
import PySimpleGUI as psg
import ddlistfunction as dd
import controller as c
import theme_variants as th
import subprocess
import vlc
from event_handler import EventHandler

#table x size:int
ts_x = 750
#table y size:int
ts_y = 25
r = False
#path:string
path = 'C:/Users/csehg'
#getting path with os module is like this
#print(os.path.expanduser('~'))

#PySimpleGUI theme is set from a list of themes, now set to
them = th.new_theme
psg.theme_add_new('MyNewTheme', them)
#Using the new generated theme
psg.theme('My New Theme')


#list of the table header type:list
fejlec = ['Extension', 'Name', 'Lastly Used', 'Size']
#list of the table values and for later use type:list
vals = []

#from ddlistfunction the calling function is called that path returns a 2dimensional list type:list
vals = list(dd.calling(path))

#this is a 2dimensional list that is used in the PySimpleGUI Frame element type:list
infocenter = [[psg.Text('Current Path:'), psg.Text('', enable_events=True, key='PTH')],
              [psg.Text('File:'), psg.Text('', enable_events=True, key='-FILENAME-')],
              [psg.Text('Size:'), psg.Text('', enable_events=True, key='-FILESIZE-')],
              [psg.Button('Back', key='Back'), psg.Button('New File', key='NF'), psg.Button('New Folder', key='NFD')],
              [psg.StatusBar('', key='STAT', size=(7, 2))],
              [psg.ProgressBar(max_value=250, size=(9,5), key='PRB')],
              [psg.Multiline('',key='VIS',size=(65, 75),horizontal_scroll=True,do_not_clear=False)]
              ]

#this is a 2dimensional list that is used in the PySimpleGUI Window element type:list
layout = [[ psg.Push(), psg.Image('C:/Users/csehg/pytry/iconexit.png', enable_events=True, pad=0, key='-EXIT-')],
          [psg.Spin(['Extension','Name','Lastly Used','Size'],initial_value='Name', enable_events=True, key='SORT')],
          [psg.Table(vals,
                     headings=fejlec,
                     size=(ts_x,ts_y),
                     justification='l',
                     key='_T01_',
                     auto_size_columns=True,
                     expand_x=False,
                     enable_events=True,
                     right_click_menu=c.folder_right_click,
                     bind_return_key=True,
                     font=('Times New Roman', th.fon_size, '')),psg.VerticalSeparator(pad=None) , psg.Frame('', infocenter), psg.VerticalSeparator(pad=None)]
          ]

window = psg.Window(
    "Table",
    layout,
    size=(1280,720),
    icon='icon/icov1.ico'
    )


while True:
    event, value = window.read()
    e = EventHandler(event)
    e.compare()
    print(event)
    
    data = {'event':None, 'value':None}
    data.update({'event':event})
    data.update({'value':value})
    print(data.items())
    data.clear()
        
    if event == '_T01_':
        kijelolt = [vals[row] for row in value[event]]

        try:
            
            if kijelolt[0][0] != '' and kijelolt[0][0] != '.exe' and kijelolt[0][0] != '.mp3':
                fhl = kijelolt[0][1] + kijelolt[0][0]
                flp = os.path.join(path, fhl)
                with open(flp, 'r') as f:
                    lines = f.read()
                    window['VIS'].print(lines)
                f.close()
                fhl = ''
                flp = ''
                
            if kijelolt[0][0] == '.exe':
                ft = kijelolt[0][1] + kijelolt[0][0]
                print(ft)
                try:
                    p = subprocess.Popen(os.path.join(path, ft))
                    return_code = p.wait()
                    print(return_code)
                    ft = ''
                except:
                    print('Not able to run')
                    
            if kijelolt[0][0] == '.mp3':
                ft = kijelolt[0][1] + kijelolt[0][0]
                print(ft)
                try:
                    if r == False:
                        l = vlc.MediaPlayer(os.path.join(path, ft))
                        l.play()
                        r = True
                    else:
                        l.stop()
                        r = False
                except:
                    print('Not able to run')
                
            if kijelolt[0][0] == '' and os.path.isdir(os.path.join(path, kijelolt[0][1] + kijelolt[0][0])):
                window['STAT'].update('Everything fine')
                direc = os.path.join(path, kijelolt[0][1])
                #print(direc)
                path = direc
                window['PTH'].update(path)
                direc = ''
                #print(path)
                vals.clear()
                #print(vals)
                vals = dd.calling(path)
                #print(vals)
                window['_T01_'].Update(values=vals)
                print(sys.getsizeof(vals))
            else:
                ...
        except (IndexError, PermissionError, FileNotFoundError, UnicodeDecodeError):
            window['STAT'].update('Everything fine')
            
    if event == 'Back':
        #print(path)
        path01, _ = os.path.split(path)
        path = path01
        window['PTH'].update(path)
        path01 = ''
        try:
            vals.clear()
            vals = dd.calling(path)
            window['_T01_'].Update(values=vals)
        except IndexError:
            print(vals)
                    
    if event == 'NF':
        print('new file creating...')
        _, values2 = psg.Window('File Creation', [ [psg.Text('Filename:')],
                                                    [psg.Input(key='IN'), psg.Combo(c.file_list, default_value='.txt', readonly=True, k='CM')],
                                                    [psg.OK(), psg.Cancel()] ]).read(close=True)
        
        if values2['IN'] == '' or values2['IN'] == None:
            psg.popup('No name specified to folder', 'Please give a name')
            values2.clear()
            pass
        else:
            fl = values2['IN'] + values2['CM']
            values2.clear()
            #print(values2)
            #print(path)
            #print(fl)
            event2, _ = psg.Window('Writer', [ [psg.Text('Do you want to write into the file?')],
                                             [psg.Button('OK'), psg.Button('No')] ]).read(close=True)
            if event2 == 'No':
                event2 = ''
                with open(os.path.join(path, fl), 'w') as fM:
                    pass
                print('file saved without writing...')
                
            else:
                event2 = ''
                print('write into the file...')
                _, values2 = psg.Window('File Writer', [ [psg.Titlebar('File Writer')],
                                                         [psg.Text('File Writer')],
                                                         [psg.Multiline('', size=(75, 45), key='MLT')],
                                                         [psg.OK(), psg.Cancel()] ]).read(close=True)
                txt = values2['MLT']
                values2.clear()
                with open(os.path.join(path, fl), 'w') as fM:
                    fM.write(txt)
                fM.close()
            
        
    if event == 'NFD':
        print('new folder creating...')
        _, values2 = psg.Window('Folder Creation', [ [psg.Text('Folder Name:')],
                                                     [psg.Input(key='INF')],
                                                     [psg.OK(), psg.Cancel()] ]).read(close=True)
        fd = values2['INF']
        if values2['INF'] == '' or fd == None:
            psg.popup('No name specified to folder', 'Please give a name')
            values2.clear()
            pass
        else:
            values2.clear()
            event2, _ = psg.Window('Write', [ [psg.Text(f'Do you want to move this folder into specified location? {path}')],
                                             [psg.Button('OK'), psg.Button('No')] ]).read(close=True)
            
            if event2 == 'No':
                creAtP = os.path.join(path, fd)
                os.mkdir(creAtP)
                psg.popup(f'New folder created at {path}', f'Path name is {creAtP}')
                creAtP = ''
                fd = ''
                event2 = ''
                print('folder created to current path....')
            else:
                _, values2 = psg.Window('Folder Creation', [ [psg.Text('Folder Name:')],
                                                         [psg.Input(key='INP')],
                                                         [psg.OK(), psg.Cancel()] ]).read(close=True)
                specP = values2['INP']
                values2.clear()
                if os.path.exists(specP) != True or specP == None:
                    psg.popup('Path you entered does not exist!', 'Please find in File Explorer and return!')
                else:
                    creaP = os.path.join(specP, fd)
                    os.mkdir(creaP)
                    psg.popup(f'New folder created at {specP}', f'Path name is {creaP}')
                    creaP = ''
                    specP = ''
                    fd = ''
                    event2 = ''
                print('folder created to specified location...')

            
    if event == 'SORT' and value['SORT'] == 'Extension':
        vals.sort(key=lambda x: x[0])
        window['_T01_'].update(values=vals)
        #print(vals)
    if event == 'SORT' and value['SORT'] == 'Name':
        vals.sort(key=lambda x: x[1])
        window['_T01_'].update(values=vals)
        #print(vals)
    if event == 'SORT' and value['SORT'] == 'Lastly Used':
        vals.sort(key=lambda x: x[2])
        window['_T01_'].update(values=vals)
        #print(vals)
    if event == 'SORT' and value['SORT'] == 'Size':
        vals.sort(key=lambda x: x[3])
        window['_T01_'].update(values=vals)
        #print(vals)
    if event in (psg.WIN_CLOSED, '-EXIT-'):
        break
    
window.close()
