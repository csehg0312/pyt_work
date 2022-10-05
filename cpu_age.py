import os
from time import time

HZ = os.sysconf(os.sysconf_names['SC_CLK_TCK'])

def proc_age_secs():
    system_stats = open('/proc/stat').readlines()
    process_stats = open('/proc/self/stat').read().split()
    for line in system_stats:
        if line.startswith('btime'):
            boot_timestamp = int(line.split()[1])
    age_from_boot_jiffies = int(line.split()[1])
    age_from_boot_timestamp = age_from_boot_jiffies / HZ
    age_timestamp = boot_timestamp + age_from_boot_timestamp
    return time() - age_timestamp