import sys
import datetime
import time
import subprocess

pid = sys.argv[1]
proc = subprocess.Popen(['ps', '-eo', 'pid,etime'], stdout=subprocess.PIPE)

proc.wait()
results = proc.stdout.readlines()

for result in results:
    try:
        result.strip()
        if result.split()[0] == pid:
            pidInfo = result.split()[1]
            #meg kell allni
            break
    except IndexError:
        pass
    
else:
    print("Process PID", pid, "does not seem to exist!")
    sys.exit(0)
    
pidInfo = pidInfo.partition("-")
if pidInfo[1] == '-':
    days = int(pidInfo[0])
    rest = pidInfo[2].split(":")
    hours = int(rest[0])
    minutes = int(intt[1])
    seconds = int(rest[2])
else:
    days = 0
    rest = pidInfo[0].split(":")
    if len(rest) == 3:
        hours = int(rest[0])
        minutes = int(rest[1])
        seconds = int(rest[2])
    elif len(rest) == 2:
        hours = 0
        minutes = int(rest[0])
        seconds = int(rest[1])
    else:
        hours = 0
        minutes = 0
        seconds = int(rest[0])
        
#kezdo ido
secondsSinceStart = days*24*3600 + hours*3600 + minutes*60 + seconds

startTime = time.time() - secondsSinceStart

print("Process started on:")
print(datetime.datetime.fromtimestamp(startTime).strftime("%a %b %d at %I:%M:%S %p"))