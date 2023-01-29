import os
import datetime
import shutil

class File:
    
    def __init__(self,suffix, name, lst_use, size, path, szulotrace):
        self.suffix = suffix
        self.name = name
        self.lst_use = lst_use
        self.size = size
        self.path = path
        self.szulotrace = szulotrace
  
    def caldate(P:str, val):
        j = os.path.join(P,val)
        T = os.path.getctime(j)
        CT = datetime.fromtimestamp(T)
        CTV = DateCall.called(CT)
        return CTV
    
    def caltype(P:str, val):
        j = os.path.join(P,val)
        _, E = os.path.splitext(j)
        if E == "":
            return ''
        #E = 'directory'
        else:
            return E
        
    def calname(P:str):
        N, _ = os.path.splitext(P)
        return N
    
    def getszulotrace(T:str):
        return 0

class Directory:
    
    def __init__(self, trace, szulo):
        self.trace = trace
        self.szulo = szulo
        
    def getatrace(F:str, szulo:str):
        Pth = os.path.join(szulo, F)
        return Pth
    
    def getszulotrace():
        return 0
    def getlistdir():
        return 0

#akarjuk a teljes meret, hasznalt, szabad meretet, 
class Drive:
    def __init__(self,DSZK:str):
        self.DSZK = DSZK
        
        @classmethod
        def getSize(cls,DSZK):
            teljes, foglalt, szabad = shutil.disk_usage(DSZK)
            teljes = self.teljes
            
            return teljes, foglalt, szabad
        
        self.full, self.used, self.free = getSize(DSZK)
        
        def calcFull(self,dsk:int):
            return (dsk // (2**30))
        

        
class DateCall:
    
    def __init__(self, date):
        self.date = date
    
    def called(ID):
        CTM = time_round(ID, datetime.timedelta(seconds=5))
        return CTM
    
class PyTable:
    def __init__(self, hossz):
        self.hossz = hossz


# class Main:
#     def __init__(self):
#         
#         
# 
# def TextEdit:
if __name__ == '__main__':
    disk = 'C:'
    adiszk = Drive(disk)
    print(adiszk.free)