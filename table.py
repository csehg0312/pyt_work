import PySimpleGUI as sg
class GUI():
    
    def __init__(self, data):
        self.layout = [
            [sg.Table(
                values=data[1:],
                headings=data[0],
                max_col_width=25,
                num_rows=20,
                alternating_row_color='green',
                key='-TABLE-',
                enable_events=True,
                enable_click_events=True,
                justification='center',
                )],
            [sg.Text("", size=(50, 1), expand_x=True, key='-Position-')]
            ]
        
        self.window = sg.Window('Table', self.layout, finalize=True)
        self.table = self.window['-TABLE-']
        self.position = self.window['-Position-']
    
    def run(self):
        while True:
            self.window['-TABLE-'].update(values = make_data(10,10))
            self.window.refresh()
            self.event, self.values = self.window.read()
            if self.event == sg.WIN_CLOSED:
                break
            elif isinstance(self.event, tuple) and self.event[0:2] == ('-TABLE-', '+CLICKED+'):       
                row, col = self.event[2]
                selection = self.values['-TABLE-']
                previous_select_row = selection[0] if selection else 'None'
                
if __name__ == '_main_':
	GUI().run()