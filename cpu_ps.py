import os 
import psutil

load1, load5, load15 = psutil.getloadavg()

cpu_usage = (load15/os.cpu_count()) * 100

print("CPU hasznalat jelenleg :", cpu_usage)