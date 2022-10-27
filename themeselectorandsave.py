import PySimpleGUI as psg
import os
import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)

plugged = "Plugged In" if plugged else "Not Plugged In"


"""
    Demo - Basic window design pattern
    * Creates window in a separate function for easy "restart"
    * Saves theme as a user variable
    * Puts main code into a main function so that multiprocessing works if you later convert to use
    
    Copyright 2020 PySimpleGUI.org
"""


# ------------------- Create the window -------------------
def make_window():
    # Set theme based on previously saved
    psg.theme(psg.user_settings_get_entry('theme', None))
    #battery = psutil.sensors_battery()
    #plugged = battery.power_plugged
    #percent = str(battery.percent)

    #plugged = "Plugged In" if plugged else "Not Plugged In"

    working_directory = os.getcwd()

    # -----  Layout & Window Create  -----
    layout = [[psg.T('This is your layout')],
              [psg.Multiline(size=(120,35), tooltip=plugged, key='_multiline_', do_not_clear=False)],
              [psg.Text('File Name'), psg.Input(size=(80, 10), key='-NAME-', do_not_clear=False), psg.OptionMenu(values=['.txt','.pdf', '.dat','.sql', '.doc', '.py', '.html', '.js', '.css'],size=(4,8),default_value='.txt',key='ftype')],
              [psg.Text('A fajl neve',key = '_savefile_', visible=True), psg.Input(size=(80, 10), key='-FILE_PATH-'),
               psg.FileBrowse(initial_folder=working_directory, font=('Times New Roman', 12), file_types = [('All files','*.*')]), psg.Button('Submit', font=('Times New Roman',12))],
              [psg.Text('Saved', key='_saved_', visible=False)],
              [psg.Button('SAVE', font=('Times New Roman', 12)), psg.Button('EXIT', font=('Times New Roman', 12)), psg.Text("", key='_BATTERY-NOW_', justification='right') ],
              [psg.OK(), psg.Button('Theme', key='-THEME-'), psg.Button('Exit')]]

    return psg.Window('Pattern for theme saving', layout)


# ------------------- Main Program and Event Loop -------------------

def main():
    window = make_window()
    multiline = psg.Multiline()
    while True:
        event, values = window.read()
        if event == psg.WINDOW_CLOSED or event == 'Exit':
            break
        if event == '-THEME-':      # Theme button clicked, so get new theme and restart window
            ev, vals = psg.Window('Choose Theme', [[psg.Combo(psg.theme_list(), k='-THEME LIST-'), psg.OK(), psg.Cancel()]]).read(close=True)
            if ev == 'OK':
                window.close()
                psg.user_settings_set_entry('theme', vals['-THEME LIST-'])
                window = make_window()
        #window['_BATTERY-NOW_'].Update(percent)
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
            txtFile = values['-NAME-'] + values['ftype']
            with open(txtFile, 'w') as file:
                data = values['_multiline_']
                file.write(data)
        file.close()
        #print(values['_multiline_'])
        window['_saved_'].Update(visible=True)

    window.close()


if __name__ == '__main__':
    main()
