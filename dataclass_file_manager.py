from dataclasses import dataclass, field
import os
from collections import deque

@dataclass
class FajlBazis:
    path:str
    fajlbazis: dict = field(init=False)
    
    def kibontas(self):
#         self.fajlbazis:dict
        self.fajlbazis.update({'Utvonal':self.path})
        self.parent,_ = os.path.split(self.path)
        self.fajlbazis.update({'SzuloUt': self.parent})
        self.fajlbazis.update({'Folders':deque([x for x in os.listdir(self.path) if os.path.isdir(os.path.join(self.path,x))])})
        return self.fajlbazis
        

path = 'C:/Users/csehg/pytry'
obj = FajlBazis(path)
obj.kibontas()
