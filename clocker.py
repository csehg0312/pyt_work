import PySimpleGUI as sg
import datetime

# KEY DEFINITIONS
# _time_ = text field that displays time


def getTime():
    return datetime.datetime.now().strftime('%p %I:%M:%S')

layout = [[sg.Text('Time: '), sg.Text('', size=(10,1), key='_time_')],
         [sg.Exit()]]

window = sg.Window('Simple Clock', layout)

while True:
    event, values = window.Read(timeout=1000)
    if event in (None, 'Exit'):
        break

    # Update '_time_' key value with return value of getTime()
    window.find_element('_time_').Update(getTime())

window.Close()