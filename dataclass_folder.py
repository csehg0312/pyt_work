from dataclasses import dataclass, field
import os

def listazd(szuloje:str, neve:str):
    f = os.path.join(szuloje, neve)
    lst = os.listdir(f)
    return lst

@dataclass
class Folder:
    szulout:str
    nev:str
    
    def __post_init__(self):
        self.mappalista:list = field(default_factory=listazd(self.szulout, self.nev))
        

amappa = Folder('C:/Users/csehg', 'pytry')
print(amappa.mappalista)
        
