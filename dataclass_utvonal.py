from dataclasses import dataclass
import os

@dataclass
class Jelen_EleresiUt:
    szulo:str 
    
    def Atiras(self):
        if os.getcwd() != self.szulo:
            self.szulo = os.getcwd()
    
    def SzuloUtvonal(self):
        self.nagyszulo, _ = os.path.split(self.szulo)
        os.chdir(self.nagyszulo)
        
    def JelenlegiDiszk(self):
        self.diszk = self.szulo[0] + self.szulo[1] + self.szulo[2]
        return self.diszk
    
    def Frissites(self, csatolt):
        self.csatolt = csatolt
        self.szulo = self.csatolt
        os.chdir(self.szulo)
        
if __name__ == '__main__':
    P:str
    P = os.path.expanduser('~')
    utv:Jelen_EleresiUt
    utv = Jelen_EleresiUt(P)
    utv.SzuloUtvonal()
    print(os.getcwd())
    utv.Atiras()
    utv.SzuloUtvonal()
    print(os.getcwd())
        
   