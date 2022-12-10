import os
import table_functions as tf
from datetime import datetime
path = 'C:/Users/csehg/Documents'

vals = os.listdir(path)
sizes = []
lastly_used = []
suffixes = []

def calcsizev2(P:str, val):
    j = os.path.join(P,val)
    S = os.path.getsize(j)
    i = 0
    unit=["b", "kb", "MB", "GB", "TB", "EB"]
    while(S>1024):
        S = round(S/1024, 2)
        i = i+1
    try:
        unitout = unit[i]
    except:
        pass
    return f"{S} {unitout}"

def caltype(P:str, val):
    j = os.path.join(P,val)
    root, E = os.path.splitext(j)
    if E == "":
        return 'directory'
        #E = 'directory'
    else:
        return E
    

def calcsize(P:str, val):
    j = os.path.join(P,val)
    S = os.path.getsize(j)
    if S <= 1024:
        pass
    else:
        S = round(S/1024, 2)
        
    return S

def caldate(P:str, val):
    j = os.path.join(P,val)
    T = os.path.getctime(j)
    
    CT = datetime.fromtimestamp(T)
    
    return CT

sor = []
oszlop = []

def list_verifier(val:list, size:list, last:list, sff:list):
    en = len(val)
    to = len(size)
    tre = len(last)
    fire = len(sff)
    if en != to:
        return 0
    elif to != tre:
        return 0
    elif tre != en:
        return 0
    elif tre != fire:
        return 0
    else:
        return en
    
def calling(path:str):
    vals = os.listdir(path)
    sizes = []
    lastly_used = []
    suffixes = []
    
    sor = []
    oszlop = []


    for l in range(len(vals)):
        if tf.itisafile(os.path.join(path, vals[l])) == True:
            sizes.append(calcsizev2(path, vals[l]))
            lastly_used.append(caldate(path, vals[l]))
            suffixes.append(caltype(path, vals[l]))
        else:
            sizes.append(" ")
            lastly_used.append(" ")
            suffixes.append('directory')
            
    num = list_verifier(vals, sizes, lastly_used, suffixes)
    print(num)

    if num != 0:
        for i in range(num):
            for j in range(1):
                sor.append(vals[i])
                sor.append(str(sizes[i]))
                sor.append(str(lastly_used[i]))
                sor.append(str(suffixes[i]))
                oszlop.append(sor)
                sor = []
           
         
            
    print(str(oszlop))
    return oszlop

if __name__ == '__main__':
    print('Success')
    print(type(calling(path)))
            
