from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class CalculatorApp(App):
    def build(self):
        # Create the layout
        layout = BoxLayout(orientation='vertical')

        # Create the display
        self.display = Button(text='0', font_size=50, background_color=[1, 1, 1, 1], color=[0, 0, 0, 1], size_hint=[1, .5])
        layout.add_widget(self.display)

        # Create the buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        # Add the buttons to the layout
        for row in buttons:
            button_row = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=30, size_hint=[.25, .25])
                button.bind(on_press=self.on_button_press)
                button_row.add_widget(button)
            layout.add_widget(button_row)

        return layout

    def on_button_press(self, button):
        if button.text == '=':
            # Calculate the result
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = 'Error'
        elif button.text == 'C':
            # Clear the display
            self.display.text = '0'
        else:
            # Append the button text to the display text
            if self.display.text == '0':
                self.display.text = button.text
            else:
                self.display.text += button.text

if __name__ == '__main__':
    CalculatorApp().run()
