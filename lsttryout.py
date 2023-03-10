import time_dependency as td
from datetime import datetime
import collections as ces
import os

def exis(p:str):
    if os.path.exists(p) == True:
        return True
    else:
        return False

def calcsizev2(P:str, val):
    j = os.path.join(P,val)
    S = os.path.getsize(j)
    SF = 0.0
    SF = float(S)
    i = 0
    unit=["b", "kb", "MB", "GB", "TB", "EB"]
    while(SF>1024):
        SF = SF/1024
        i = i+1
    try:
        unitout = unit[i]
        SF = round(S,2)
    except:
        pass
    return f'{SF} {unitout}'

def calname(P:str, val):
    j = os.path.join(P,val)
    if exis(j) == True:
        N, _ = os.path.splitext(val)
        return N
    else:
        return 0

def caltype(P:str, val):
    j = os.path.join(P,val)
    if exis(j) == True:
        _, E = os.path.splitext(j)
        return E
    else:
        return 0
    
def caldate(P:str, val):
    j = os.path.join(P,val)
    T = os.path.getctime(j)
    if exis(j) == True:
       T = os.path.getmtime(j)
       CT = datetime.fromtimestamp(T)
       CTV = td.called(CT)
       return f'{CTV}'
    
    else:
        return 0
    
def calc_num(pth:str):
    val = os.listdir(pth)
    return len(val)



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
    
def oslist(path:str):
    val = []*osnum(path)
    val = os.listdir(path)
    return val
    
def osnum(path:str):
    
    h = len(os.listdir(path))
    return h
    
def callmap(path:str):
    val = oslist(path)
    val.sort()
#     loszlop = []*len(val)
#     lsor = []*4

#Creating the one run permanent data dictionary that will be used to store the lists of table element
    data = {'Name': str, 'Extension':str, 'Date': str, 'Size':int, 'Unit':str}
    print('Data dictionary created...')
    map(caltype(path,), val)
    map(calname(path,), val)
    map(caldate(path,val), val)
    map(calcsizev2(path,val), val) 
#     for oszlop in range(len(val)):
#         for sor in range(4):
#             if os.path.isdir(val[oszlop]):
#                 lsor.append('', val[oszlop], '', '')
#             else:
#                 lsor.append(map(caltype(path, val[oszlop]), val[oszlop]),
#                            map(calname(path, val[oszlop]), val[oszlop]),
#                            map(caldate(path, val[oszlop]), val[oszlop]),
#                            map(calcsizev2(path, val[oszlop]), val[oszlop])
#                            )
#             loszlop.append(sor)
#             lsor.clear()

            
    
    return 1

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
        if os.path.isfile(os.path.join(path, vals[l])) == True:
            sizes.append(calcsizev2(path, vals[l]))
            lastly_used.append(caldate(path, vals[l]))
            suffixes.append(caltype(path, vals[l]))
        else:
            sizes.append(" ")
            lastly_used.append(" ")
            suffixes.append('')
            
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

# if __name__ == '__main__':
#     path = 'C:/Users'
#     lisy = ces.
#     print(lisy)