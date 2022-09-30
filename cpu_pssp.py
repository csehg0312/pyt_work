import psutil

print("CPU hasznalat jelenleg: ", psutil.cpu_percent(interval=4))
print("CPU alap: ", psutil.cpu_freq(percpu=True))