import PySimpleGUI as psg

psg.theme('Reddit')
psg.set_options(font = 'Franklin 14', button_element_size = (6,3))
button_size = (6,3)

layout = [[psg.Text('output', key='-OUTPUT-')],
          [psg.Button('Enter', expand_x = True), psg.Button('Clear', expand_x = True)],
          [psg.Button(9, size=button_size), psg.Button(8, size=button_size), psg.Button(7, size=button_size), psg.Button('/', size=button_size)],
          [psg.Button(6, size=button_size), psg.Button(5, size=button_size), psg.Button(4, size=button_size), psg.Button('*', size=button_size)],
          [psg.Button(3, size=button_size), psg.Button(2, size=button_size), psg.Button(1, size=button_size), psg.Button('-', size=button_size)],
          [psg.Button(0, expand_x = True), psg.Button('.', size=button_size), psg.Button('+', size=button_size)]
          ]

window = psg.Window('Calculator', layout)

while True:
    event, values = window.read(timeout=50)
    #print(event)
    
    match event:
        case '__TIMEOUT__':
            pass
        case other:
            window['-OUTPUT-'].update(event)
    if event == psg.WIN_CLOSED:
        break
    
window.close()