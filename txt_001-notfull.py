import PySimpleGUI as psg

psg.theme('SystemDefault')

menu_def=['&Fájl', ['&Új fájl', '&Megnyitás', '&Modul megnyitása', '---', '!&Utóbbi fájlok', 'Be&zárás']], ['&Mentés', ['&Fájl mentése', 'Fájl &mentés mint', 'Kópia &mentése'  ]], ['&Szerkesztés', ['&Kivágás', '&Másolás', '&Beillesztés']]

layout=[[psg.Menu(menu_def, background_color='lightsteelblue',text_color='navy', disabled_text_color='yellow', font='Verdana', pad=(10,10))],
        [psg.ButtonMenu('', [['nf', 'op', 'om', '---', 'rf', 'cl'], ['New File', 'Open', 'Open Module', '---', 'Recent Files', 'Close']] image_filename='icon/plus-50.png', border_width=5, psg.ButtonMenu('', [['rm', 'rc', 'sm', 'ps'], ['Run', 'Run Modeule', 'Shell', 'Python Module']], image_filename='icon/cut-50.png', background_color='teal' ), psg.ButtonMenu('Terminate', [['ex', 'cl','---','ab'],['Exit', 'Close','---','About us...']]))],
        [psg.Multiline(size=(80,10),tooltip='Write your Text here')],
        [psg.Text('File Name'),psg.Input(),psg.OptionMenu(values=['.txt','.pdf','.gif', '.jpg','.mp4','.gif','.dat','.sql'],size=(4,8),default_value='.doc',key='ftype')],
        [psg.Button('MENTÉS', font=('Times New Roman',12)),psg.Button('KILÉPÉS', font=('Times New Roman',12))]]

window = psg.Window('Text editor', layout)

events, values = window.read()

window.close()