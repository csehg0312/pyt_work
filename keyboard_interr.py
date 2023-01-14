import PySimpleGUI as sg
import keyboard
from time import sleep

keyboard.get_hotkey_name() # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

layout = [
    [
        sg.Button('', enable_events=True, key=(1, 1))
    ]
        ]

window = sg.Window('Image Browser', layout,
                   return_keyboard_events=False, finalize=True, auto_size_buttons=False, use_default_focus=True,
                   resizable=True, size=(100, 100))

while True:

    event, values = window.read(timeout=0)

    if event == "Exit" or event == sg.WINDOW_CLOSED:
        break

    if keyboard.is_pressed('ctrl+z'):
        print("++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++")

    sleep(0.01)
window.close()