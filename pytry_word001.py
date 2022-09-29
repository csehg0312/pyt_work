import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [[sg.Text('Your typed characters appear here:'),
           sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Display'), sg.Button('Exit')]]

window = sg.Window('Bevezetes', layout)

while True:
	event,values = window.read()
	print(event,values)
	
	if event in (None, 'Exit'):
		break
	
	if event == 'Display':
		#Updateli az outputot
		#hogy erteke az input eleme legyen
		window['-OUTPUT-'].update(values['-IN-'])

window.close()
