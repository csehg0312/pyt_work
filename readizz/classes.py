import os
import shutil
import datetime

class File:
    def __init__(self, name, size, size_in, lst_mod, suffix, path, szulopath):
        self.name = name
        self.size = size
        self.size_in = size_in
        self.lst_mod = lst_mod
        self.suffix = suffix
        self.path = path
        self.szulopath = szulopath
    
    def __str__(self):
        return f"{self.name} \nSize:{self.size} {self.size_in} \nLastly used:{self.lastly_used}"

