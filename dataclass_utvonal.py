from dataclasses import dataclass
import os

@dataclass
class Jelen_EleresiUt:
    szulo:str
    mappa:str
    
    def Atiras(self):
        if self.szulo != os.getcwd():
            os.chdir(self.szulo)
    
    def SzuloUtvonal(self):
        self.nagyszulo, _ = os.path.split(self.szulo)
        os.chdir(self.nagyszulo)
        
    def UtvonalCsatlakozas(self):
        self.gyermek = os.path.join(self.szulo, self.mappa)
        os.chdir(self.gyermek)
        
    def JelenlegiDiszk(self):
        self.diszk = self.szulo[0] + self.szulo[1] + self.szulo[2]
        return self.diszk
        
if __name__ == '__main__':
    p = 'C:/Users/csehg/Documents'
    mappa = 'Obsidian'
    P = Jelen_EleresiUt(p, mappa)
    print(os.getcwd())
    P.UtvonalCsatlakozas()
    print(os.getcwd())
    l = P.JelenlegiDiszk()
    print(l)