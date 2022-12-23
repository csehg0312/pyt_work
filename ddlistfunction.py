import os
import table_functions as tf
from datetime import datetime
import time_dependency as td
path = 'C:/Users/csehg/Documents'

def calcsizev2(P:str, val):
    j = os.path.join(P,val)
    S = os.path.getsize(j)
    i = 0
    unit=["b", "kb", "MB", "GB", "TB", "EB"]
    while(S>1024):
        S = S/1024
        i = i+1
    try:
        unitout = unit[i]
        S = round(S,2)
    except:
        pass
    return f"{S} {unitout}"

def calname(P:str):
    N, _ = os.path.splitext(P)
    
    return N

def caltype(P:str, val):
    j = os.path.join(P,val)
    _, E = os.path.splitext(j)
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
        S = S/1024
    S = round(S,2)
    return S

def caldate(P:str, val):
    j = os.path.join(P,val)
    T = os.path.getctime(j)
    
    CT = datetime.fromtimestamp(T)
    CTV = td.called(CT)
    return CTV

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
    
def calling_from_lst(LsT:list, pth:str):
    
    vlslen = len(LsT)
    
    sizes = []*vlslen
    lastly_used = []*vlslen
    suffixes = []*vlslen
    
    sor = []*4
    oszlop = []*vlslen
    for l in range(vlslen):
        if tf.itisafile(os.path.join(pth, LsT[l])) == True:
            sizes.append(calcsizev2(pth, LsT[l]))
            lastly_used.append(caldate(pth, LsT[l]))
            suffixes.append(caltype(pth, LsT[l]))
        else:
            sizes.append(" ")
            lastly_used.append(" ")
            suffixes.append('directory')
            
    num = list_verifier(LsT, sizes, lastly_used, suffixes)
        
    if num != 0:
        for i in range(num):
            for j in range(1):
                sor.append(LsT[i])
                sor.append(str(sizes[i]))
                sor.append(str(lastly_used[i]))
                sor.append(str(suffixes[i]))
                oszlop.append(sor)
                sor = []
            
        return oszlop
    
    
def calling(path:str):
    try:
        vals = os.listdir(path)
        vals.sort()
        valslen = len(vals)
    except:
        return 0
    sizes = []*valslen
    lastly_used = []*valslen
    suffixes = []*valslen
    
    sor = []*4
    oszlop = []*valslen


    for l in range(valslen):
        if tf.itisafile(os.path.join(path, vals[l])) == True:
            sizes.append(calcsizev2(path, vals[l]))
            lastly_used.append(caldate(path, vals[l]))
            suffixes.append(caltype(path, vals[l]))
        else:
            sizes.append(" ")
            lastly_used.append(" ")
            suffixes.append('directory')
            
    num = list_verifier(vals, sizes, lastly_used, suffixes)
    #print(num)

    if num != 0:
        for i in range(num):
            for j in range(1):
                sor.append(str(suffixes[i]))
                sor.append(calname(vals[i]))
                sor.append(str(lastly_used[i]))
                sor.append(str(sizes[i]))
                oszlop.append(sor)
                sor = []
           
         
            
    #print(str(oszlop))
    return oszlop

def calc_num(pth:str):
    val = os.listdir(pth)
    return len(val)

#def sorter(lstts:list, num:int):

def pth_verifier(Pth:str):
    if os.path.lexists(Pth) == True:
        return True
    else:
        return False

def path_splitter(pth:str):
    if pth_verifier(pth) == True:
        root, _ = os.path.split(pth)
        #print(root)
        return root
    else:
        return 0

def path_create(pTh:str, nxtpth:str):
    if pth_verifier(pTh) == True:
        nexpt = os.path.join(pTh, nxtpth)
        if pth_verifier(nexpt) == True:
            return nexpt
        else:
            return 0
    else:
        return 0
    
    

if __name__ == '__main__':
    print('Success')
    pth = 'C:/Users/csehg/Documents/Arduino/libraries'
    lst = os.listdir(pth)
    print(calling_from_lst(lst, pth))
    #caldate('ddlistfunction.py', 'C:/Users/csehg/pytry')
            