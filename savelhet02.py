import PySimpleGUI as psg
import os
import psutil
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)

plugged = "Plugged In" if plugged else "Not Plugged In"

working_directory = os.getcwd()
psg.theme('SystemDefault')

layout = [[psg.Multiline(size=(120,35), tooltip=plugged, key='_multiline_', do_not_clear=False)],
          [psg.Text('File Name'), psg.Input(size=(80, 10), key='-NAME-', do_not_clear=False), psg.OptionMenu(values=['.txt','.pdf', '.dat','.sql', '.doc', '.py', '.html', '.js', '.css'],size=(4,8),default_value='.txt',key='ftype')],
          [psg.Text('A fajl neve',key = '_savefile_', visible=True), psg.Input(size=(80, 10), key='-FILE_PATH-'),
           psg.FileBrowse(initial_folder=working_directory, font=('Times New Roman', 12), file_types = [('All files','*.*')]), psg.Button('Submit', font=('Times New Roman',12))],
          [psg.Text('Saved', key='_saved_', visible=False)],
          [psg.Button('SAVE', font=('Times New Roman', 12)), psg.Button('EXIT', font=('Times New Roman', 12)), psg.Text("", key='_BATTERY-NOW_', justification='right') ]
          ]

window = psg.Window("Ablak", layout, size=(900,700), element_justification='l')
multiline = psg.Multiline()

while True:
    event, values = window.read()
    window['_BATTERY-NOW_'].Update(percent)
    if event == 'Submit':
        thisFile = values['-FILE_PATH-']
        with open(thisFile, 'r') as file:
            datao = file.read()
            #encoded_bytes = datao.encode('utf-8', 'replace')
            #datao_dec = datao.decode('utf-8', 'replace')
            window['_multiline_'].print(datao)
            window['-NAME-'].Update(values['-FILE_PATH-'])
        file.close()
    if event == 'SAVE':
        #psg.Print('Saved')
        #multiline.print(" ")
        #multiline.print("Saved")
        txtFile = values['-NAME-'] + values['ftype']
        #print(txtFile)
        #print(values['-NAME-'])
        with open(txtFile, 'w') as file:
            data = values['_multiline_']
            file.write(data)
        file.close()
        #print(values['_multiline_'])
        window['_saved_'].Update(visible=True)
    if event in (psg.WIN_CLOSED, 'EXIT'):
        print('Exiting...')
        break
window.close()
