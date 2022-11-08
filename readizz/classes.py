import os

class File:
    def __init__(self, name, size, size_in, lastly_used):
        self.name = name
        self.size = size
        self.size_in = size_in
        self.lastly_used = lastly_used
    
    def __str__(self):
        return f"{self.name} \nSize:{self.size} {self.size_in} \nLastly used:{self.lastly_used}"

