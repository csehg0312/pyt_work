import os
import PySimpleGUI as psg
 
# Get the list of all files and directories
 
#print("Files and directories in '", path, "' :")
path = ""
currentPath = []
layout = [[psg.InputText(key='_IN_', size=(20,1)), psg.Button('Read')], [psg.Listbox(values=[], key="_listen_", size=(15, 10), enable_events=True)], [psg.Multiline('', key='_multiline_', size=(25,10), do_not_clear=True)]]



window = psg.Window('Listed', layout, size=(500,500))
 
while True:
 	event, values = window.read()
 	#window['_multiline_'].print(event)
 	if event == psg.WIN_CLOSED:
 		break
 	if event == 'Read':
 		path = values['_IN_']
 		try:
 			dir_list = os.listdir(path)
 			items = len(dir_list)
 			for i in range(items):
 				#window['_multiline_'].print(dir_list[i])
 				window['_listen_'].update(dir_list)
 		except:
 			window['_multiline_'].print('Permission is denied')
 	if event == '_listen_':
 		#path = values['_IN_']
 		window['_multiline_'].print('Double clicked')
 		#window['_multiline_'].print(values['_listen_'])
 		curr = values['_listen_']
 		currSO = ""
 		currS = currSO.join(curr)
 		path = path + "/" + currS
 		window['_multiline_'].print(path)
 		try:
 			dir_list = os.listdir(path)
 			items = len(dir_list)
 			for i in range(items):
 				#window['_multiline_'].print(dir_list[i])
 				window['_listen_'].update(dir_list)
 		except:
 			window['_multiline_'].print('Permission is denied')