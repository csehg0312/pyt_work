import PySimpleGUI as psg
#set the theme for the screen/window
psg.theme('SystemDefault')
#menu_def=['&File', ['&New File', '&Open...','Open &Module','---', '!&Recent Files','C&lose']],['&Save',['&Save File', 'Save &As','Save &Copy'  ]],['&Edit', ['&Cut', '&Copy', '&Paste']]
#define layout
layout=[#[psg.Menu(menu_def, background_color='lightsteelblue',text_color='navy', disabled_text_color='yellow', font='Verdana', pad=(10,10))],
        [psg.ButtonMenu('', [['nf', 'op','om','---','rf','cl'],['New File', 'Open','Open Module','---','Recent Files','Close']],image_filename ='icon/plus-50.png',border_width=1, background_color='white'),psg.ButtonMenu('', [['rm', 'rc','sm','ps'],['Run', 'Run Module','Shell','Python module']],image_filename ='icon/cut-50.png', border_width=1, background_color='white'),psg.ButtonMenu('Terminate', [['ex', 'cl','---','ab'],['Exit', 'Close','---','About us...']], border_width=1, background_color='gray')],
        [psg.Multiline(size=(80,10),tooltip='Write your Text here')],
        [psg.Text('File Name'),psg.Input(),psg.OptionMenu(values=['.txt','.pdf','.gif', '.jpg','.mp4','.gif','.dat','.sql'],size=(4,8),default_value='.doc',key='ftype')],
        [psg.Button('SAVE', font=('Times New Roman',12)),psg.Button('CANCEL', font=('Times New Roman',12))]]
#Define Window
win =psg.Window('Your Custom Editor',layout)
#Read  values entered by user
events,values=win.read()
#close first window
win.close()
