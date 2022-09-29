import PySimpleGUIQt as sg
#import PySimpleGUIWx as sg
#import PySimpleGUI as sg

menu_def = ['BLANK', ['&Open', '---', '&Save', ['1', '2', ['a', 'b']], '&Properties', 'E&xit']]

tray = sg.SystemTray(menu=menu_def, filename=r'default.ico')

while True:
	menu_item = tray.read()
	print(menu_item)
	if menu_item == 'Exit':
		break
	elif menu_item == 'Open':
		sg.popup('Menu item chosen', menu_item)