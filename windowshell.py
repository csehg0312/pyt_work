import cmd, sys
import PySimpleGUI as sg
from turtlecmd import TurtleShell

shell = TurtleShell()

layout = [
	[sg.Text("Hello from Turtle")],
    [sg.Multiline('', key='MLT')],
	[sg.Button("OK")]
]

#create the window
window = sg.Window("Demo", layout)

#create an event loop
while True:
	event, values = window.read(timeout=100)
	#End of program if user closes window or 
	#presses the OK button
	window['MLT'].print(shell.cmdloop())
	if event == "OK" or event == sg.WIN_CLOSED:
		break

window.close()