from dataclasses import dataclass, field
import ddlistfunction as dd

@dataclass
class File:
    path:str
    name:str
    