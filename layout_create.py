import PySimpleGUI as psg
def layout_creator(nev:str, teljes:int, Pid:int):
    pre = [[psg.Text(nev)],
           [psg.StatusBar('Connected'), psg.ProgressBar(max_value=teljes, key=f'DSK{Pid}')]
           ]
    return pre


def pop_from_layout(lay:list, pid:int):
    _ = lay.pop(pid)
    if lay.__len__() == 0:
        return 0
    else:
        return lay