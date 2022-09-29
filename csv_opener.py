import PySimpleGUI as psg
import csv, os

working_directory = os.getcwd()

layout = [
        [psg.Text('valaszd ki a CSV fajlt:')],
        [psg.InputText(key='-FILE_PATH-'),
        psg.FileBrowse(initial_folder=working_directory, file_types = [('CSV Files','*.csv')])],
        [psg.Button('Submit'), psg.Exit()]
    ]

window = psg.Window('Feltoltes', layout)

def display_csv_array(csv_address):
    file = open(csv_address)
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    rows = []
    for row in csv_reader:
        rows.append
    file.close
    return rows

while True:
    event, values = window.read()
    if event in (psg.WIN_CLOSED, 'Exit'):
        break
    
    elif event == 'Submit':
        csv_address = values['-FILE_PATH-']
        print(display_csv_array(csv_address))

window.close()