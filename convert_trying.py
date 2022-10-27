import PySimpleGUI as psg

layout = [
    [psg.Text('Convert from:'), psg.Spin(['km to miles', 'kg to lbs'], key='-CHOOSE-', enable_events = True)],
    [psg.Button('Converter', key='-CONVERT-'), psg.Input(key='-INP-')],
    [psg.Text("", key='-OUT-'), psg.Text("", key='-SHOW-')]
    ]

window = psg.Window("Converter", layout)

while True:
    event, values = window.read(timeout=50)
    #window['-SHOW-'].Update(str(values['-CHOOSE-']))
    
    if event == psg.WIN_CLOSED:
        break
    if event == '-CONVERT-':
        #print(values['-INP-'])
        input_val = values['-INP-']
        if input_val != "":
            if input_val.isnumeric():
                
                window['-SHOW-'].update("")
                if values['-CHOOSE-'] != 'km to miles':
                    #print('Conversion kg to lbs)
                    num = int(input_val)
                    num = (num * 2.20462)
                    val = str(num)
                    print(num, 'lbs')
                    #window('-OUT-').update(val)
                    num = 0
                else:
                    #print('Conversion from km to miles')
                    num = int(input_val)
                    num = (num * 0.6214)
                    print(num, 'miles')
                    num = 0
            else:
                #print('Input is not numeric')
                window['-SHOW-'].update('Please write a number')
                
        else:
            window['-SHOW-'].update('Please add a value')
            #print('Add a value')
        
    
window.close()