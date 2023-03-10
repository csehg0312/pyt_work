from dataclasses import dataclass, field
import os

def listazd(szuloje:str):
    lst = os.listdir(szuloje)
    return lst

@dataclass
class Folder:
    szulout:str
    
    def __post_init__(self):
        self.mappalista:list = field(default_factory=listazd(self.szulout))
        

# amappa = Folder('C:/Users/csehg', 'pytry')
# print(amappa.mappalista.default_factory)
        
