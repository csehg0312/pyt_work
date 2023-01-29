from dataclasses import dataclass, field
import lsttryout as fun
import os
#dataclass_file()

@dataclass
class File:
    ut: str
    fajl: str
    
    def __post_init__(self):
        self.hely:str
        self.meret:float
        self.egysege:str
        self.modositdate:str
        self.nev: str = field(default_factory=fun.calname(self.ut, self.fajl))
        self.bovitmeny: str = field(default_factory=fun.caltype(self.ut, self.fajl))
        

afajl = File('C:/Users/csehg/pytry', 'dataclass_file.py')
print(f'{afajl.nev.default_factory} {afajl.bovitmeny.default_factory}')
        

