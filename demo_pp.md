---
marp:true
theme: gaia
---

# PySimpleGUI first impressions :snake:
By: Gabriel Cseh

---
# Slide Header
A python plugin for creating a GUI for Python

Possible to create:
* File explorer
* Image Editor
* ...

---
# First program
We start by a single windowed program like this:
```
import PySimpleGUI as psg

#creating a layout for the window like this
layout = [
        [psg.Text('Hello')],
        [psg.Button('Exit')]
        ]

window = psg.Window('Hello Window', layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED():
        break

window.close()