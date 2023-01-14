import os
import readizz.classes as cl

path = 'C:/Users/csehg/pytry'

vals = os.listdir(path)
#vals.sort()

for fl in range(len(vals)):
    if os.path.isfile(vals[fl])==False:
        print('D')
    else:
        print('file')