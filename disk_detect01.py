import PySimpleGUI as psg
import os.path
import layout_create as lc
import collections as ces

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
    layout = [[psg.Text("", key='_inDrive_')],
              [psg.Column([[]], key='TEXTS')],
              [psg.Button('CANCEL'), psg.Button('Refresh')]]
    window = psg.Window('Disk detector', layout)
    outdrive = ces.deque([])
    while True:
        event, values = window.read(timeout=100)
        if event == 'Refresh':
            ...

        try:
            uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
            #print(uncheckeddrives)
            for x in (x for x in uncheckeddrives if x not in outdrive):
                print(outdrive)
                outdrive.append(x)
                print(outdrive)
                en = outdrive.copy()
                for _ in en:
                    print(en.pop())


            for x in (x for x in outdrive if x not in uncheckeddrives):
                print(outdrive)
                outdrive.pop()
                print(outdrive)
                en = outdrive.copy()
                for _ in en:
                    print(en.pop())

            window['_inDrive_'].Update()
            x = diff(uncheckeddrives, drives)
            if x:
                #print("New drives:         " + str(x))
                det()
            x = diff(drives, uncheckeddrives)
            if x:
                #print("Removed drives:     " + str(x))
                rem()
            drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
        except:
            pass
            
        if event == 'CANCEL' or event == psg.WIN_CLOSED:
            break
    window.close()