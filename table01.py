import PySimpleGUI as sg



# Table related items
headings=['PK ','DATE  ','OPEN  ','HIGH  ','LOW   ','CLOSE  ','VOLUME ']
visible=[0,1,1,1,1,1,1]
vals=[
    [1,2,3,4,5,6,7],
    [7,6,5,4,3,2,1],
    [6,3,5,1,2,7,8],
    [9,5,3,6,3,2,7],
    [2,5,2,6,1,8,7]
]

layout=[
    [sg.Table(vals,key='table1', headings=headings, visible_column_map=visible,enable_events=True,select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
]

win=sg.Window('Table event test',layout,finalize=True)

while True:
    event, values = win.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'table1':
        print('Processing table1 event')
        data_selected = [vals[row] for row in values[event]]
        print(data_selected)

        # Now I would like to reset the selection to row 0.
        #win[event].update(select_rows=[0])  # <============================ Uncomment here for an event chain reaction
    else:
        print(f'This event ({event}) is not yet handled.')