import PySimpleGUI as psg
import shutil

total, used, free = shutil.disk_usage("/")
ctotal = total // (2**30)
print(ctotal)
cused = used // (2**30)
print(cused)
cfree = free // (2**30)

layout = [[psg.Text('Current Disk use'), psg.Text('', key=('_theProgress_')), psg.Text('GB')],
          [psg.ProgressBar(ctotal, orientation='h', size=(20,20), key='_progressbar_')],
          [psg.Cancel()]]

window = psg.Window('ProgressMeter here:', layout)

progress_bar = window['_progressbar_']
while True:
  
    event, values = window.read(timeout=10)
    window['_theProgress_'].Update(cused)
    progress_bar.UpdateBar(cused)
    if event == 'Cancel' or event == psg.WIN_CLOSED:
        break
        
    
window.close()