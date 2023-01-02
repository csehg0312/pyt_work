import os
import datetime
import shutil

class File:
    
    def __init__(self,suffix, name, lst_use, size, ut, szolopath):
        self.suffix = suffix
        self.name = name
        self.lst_use = lst_use
        self.size = size
		self.ut = ut
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
        	return 'directory'
        #E = 'directory'
    	else:
        	return E
	def calname(P:str):
    	N, _ = os.path.splitext(P)
    
    	return N
    def getszulotrace(T:str)
        

class Directory:
    
    def __init__(self, ut, szulo):
		self.ut = ut
		self.szulo = szulo
		
	def getatrace():
	
	def getszulotrace():
	
	def getlistdir():
	
	

class Drive:
	
	def __init__(self, teljes, hasznal, szabad, suff):
		self.teljes = teljes
		self.hasznal = hasznal
		self.szabad = szabad
		self.suff = suff
        
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
#     