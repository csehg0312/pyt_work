import PySimpleGUI as psg
import os.path

def diff(list1,list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference

def det():
    print('New drive introduced')
    
def rem():
    print('Drive disconnected')
    
dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
#print(drives)

if __name__ == '__main__':
    layout = [[psg.InputText("", key='_inDrive_', do_not_clear=False)],
          [psg.Button('CANCEL')]]
    window = psg.Window('Disk detector', layout)
    while True:
        event, values = window.read(timeout=100)
        unckeckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
        window['_inDrive_'].Update(unckeckeddrives)
        x = diff(unckeckeddrives, drives)
        if x:
            #print("New drives:         " + str(x))
            det()
        x = diff(drives, unckeckeddrives)
        if x:
            #print("Removed drives:     " + str(x))
            rem()
        drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
        if event == 'CANCEL' or event == psg.WIN_CLOSED:
            break
    window.close()