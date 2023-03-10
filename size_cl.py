import os
from filefolder_manager import simple_data
from collections import deque


def sizeCal(path):
    return os.path.getsize(path)

path = 'C:/Users/csehg/Documents'

dic = simple_data(path)

flDeq = dic.get('Files')
sizeDeq = deque([],maxlen=len(flDeq))
#flList = list(flDeq)
#print(list(flList))
for i in range(len(flDeq)):
    sizeDeq.append(sizeCal(os.path.join(path, flDeq[i])))
    
print(list(sizeDeq))
