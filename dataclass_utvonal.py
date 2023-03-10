from dataclasses import dataclass
import os

@dataclass
class Jelen_EleresiUt:
    szulo:str 
    
    def Atiras(self):
        if self.szulo != os.getcwd():
            os.chdir(self.szulo)
    
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
    ...
        
   