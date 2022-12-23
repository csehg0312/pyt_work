import os
import PySimpleGUI as psg
import table_functions as tf
import ddlistfunction as dd
import mod_list as ml


ts_x = 750
ts_y = 25
path = 'C:/Users/csehg/Documents'
#print(os.path.expanduser('~'))
tablework = os.listdir(path)
psg.theme('SystemDefault')

parent_path = dd.path_splitter(path)
print(parent_path)

fejlec = ['Extension', 'Name', 'Lastly Used', 'Size']

vals = dd.calling(path)

infocenter = [[psg.Text('File:'), psg.Text('', enable_events=True, key='-FILENAME-')],
              [psg.Text('Size:'), psg.Text('', enable_events=True, key='-FILESIZE-')]
              ]


layout = [[ psg.Push(), psg.Image('C:/Users/csehg/pytry/iconexit.png', enable_events=True, pad=0, key='-EXIT-')],
          [psg.Table(vals,
                     headings=fejlec,
                     size=(ts_x,ts_y),
                     key='_T01_',
                     auto_size_columns=True,
                     expand_x=False,
                     enable_events=True, enable_click_events=True), psg.Frame('', infocenter)]
          ]

window = psg.Window(
    "Table",
    layout,
    size=(1280,720)
    )

while True:
    event, value = window.read()
    #print(event)
    
    if event == ('_T01_','+CLICKED+',(int,0)):
        print('clicked')
    
    if event == '_T01_':
        kijelolt = [vals[row] for row in value[event]]
        print(kijelolt)
        #print(vals[value['_T01_'][0]])
        window['-FILENAME-'].update(kijelolt[0][1])
        window['-FILESIZE-'].update(kijelolt[0][3])
        #print(dd.path_create(path, kijelolt[0][0]))
        nextpt = dd.path_create(path, kijelolt[0][0])
        print(nextpt)
        fl = tf.itisafile(nextpt)
        if fl == True:
            pass
        else:
            #valn = dd.calling(nextpt)
            #valn = ml.modify_list(vals, len(vals))
            #print(str(valn))
            try:
                #window['_T01_'].Update(valn)
                #window['_T01_'].set_focus()
                print('directory')
                print(kijelolt[0][0])
                
            except IndexError:
                print('List out of range', kijelolt[0][0])
            
    if event == ('_T01_', '+CLICKED+', (-1, 0)):
        print('Extension')
    if event == ('_T01_', '+CLICKED+', (-1, 1)):
        print('Name')
    if event == ('_T01_', '+CLICKED+', (-1, 2)):
        print('Lastly Used')
    if event == ('_T01_', '+CLICKED+', (-1, 3)):
        print('Size')
    
    if event in (psg.WIN_CLOSED, '-EXIT-'):
        break
    
window.close()
