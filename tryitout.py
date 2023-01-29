import PySimpleGUI as psg

fejlec = ['Name', 'Extension', 'Size']
data = [['szabad', 'extense', '6kB']]
cal = 0

layout = [[psg.Table(data, headings=fejlec, key='T01', enable_events=True)]]

window = psg.Window('Table',layout)

while True:
    event, value = window.read()
    print(event)
    if event == psg.WIN_CLOSED:
        break
    if event == 'T01':
        kijelolt = [data[row] for row in value[event]]
        print(kijelolt)
    
window.close()