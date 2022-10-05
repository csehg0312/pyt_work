import psutil

while True:
    print("CPU hasznalat jelenleg: ", psutil.cpu_percent(interval=8))
    print("CPU alap: ", psutil.cpu_freq(percpu=True))
    