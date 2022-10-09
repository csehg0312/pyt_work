import PySimpleGUI as sg
import datetime
import shutil



# KEY DEFINITIONS
# _time_ = text field that displays time
total = shutil.disk_usage("/")
ctotal = total // (2**30)

def getTime():
    return datetime.datetime.now().strftime('%p %I:%M:%S')

layout = [[sg.Text('Jelenlegi diszk hasznalat:'), sg.Text('', key=('_theProgress_'))],
          [sg.ProgressBar(ctotal, orientation='h', size=(20,20), key='_progressbar_')],
          [sg.Text('Time: '), sg.Text('', size=(10,1), key='_time_')],
          [sg.Exit()]]

window = sg.Window('Simple Clock with progress', layout)

while True:
    event, values = window.Read(timeout=1000)
    used, free = shutil.disk_usage("/")
    cused = used // (2**30)
    cfree = free // (2**30)
    

    # Update '_time_' key value with return value of getTime()
    window.find_element('_time_').Update(getTime())
    window['_theProgress_'].Update(cused)
    progress_bar.UpdateBar(cused)
    if event in (None, 'Exit'):
        break

window.Close()