import PySimpleGUI as psg
import psutil
import shutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)

layout = [[psg.Text("CPU performance checker"), psg.Button('GET'), psg.Button('GETSSD')]]

window = psg.Window("CPU current performance", layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    if event == 'GET':
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        plugged = "Plugged In" if plugged else "Not Plugged In"
        print("CPU----")
        print("CPU hasznalat jelenleg: ", psutil.cpu_percent(interval=4))
        print("CPU alap: ", psutil.cpu_freq(percpu=True))
        print("BATTERY----")
        print(percent+'% | '+plugged)
        print("----")
    if event == 'GETSSD':
        total, used, free = shutil.disk_usage("/")

        print('Total: %d GiB' % (total // (2**30)))
        print('Used: %d GiB' % (used // (2**30)))
        print('Free: %d GiB' % (free // (2**30)))
        print("---")
        
    
window.close()