import PySimpleGUI as psg
import Olayout
import helpandfunc

#layout01 = layouts.layoutv1

window = Olayout.windowv1

while True:
    event, values = window.read()
    if event in (psg.WIN_CLOSED,'Cancel'):
        break

window.close()