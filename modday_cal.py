import os
from filefolder_manager import simple_data
from collections import deque

def calDay(P):
    return os.path.getmtime(P)

path = 'C:/Users/csehg'

dic = simple_data(path)

flDeq = dic.get('Files')
moddayDeq: deque
moddayDeq = deque([],maxlen=len(flDeq))

for i in range(len(flDeq)):
    moddayDeq.append(calDay(os.path.join(path, flDeq[i])))
    
print(list(moddayDeq))