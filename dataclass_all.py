from dataclasses import dataclass, field
import os
import shutil

@dataclass
class Drive:
    DSZK:str
    TeliBit:int
    FoglaltBit:int
    SzabadBit:int
    
    def __post_init__(self):
        self.Teljes: int = field(default_factory=calculateSize(self.TeliBit))
        self.Foglalt: int = field(default_factory=calculateSize(self.FoglaltBit))
        self.Szabad: int = field(default_factory=calculateSize(self.SzabadBit))
        

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
        

@dataclass
class Folder:
    szulout:str
    nev:str
    
    def __post_init__(self):
        self.mappalista:list = field(default_factory=listazd(self.szulout, self.nev))
        

