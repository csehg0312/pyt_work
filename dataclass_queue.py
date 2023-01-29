from dataclasses import dataclass

@dataclass
class Forgo():
    hossza: int
    def __post_init__(self):
        self.forgas:list = [None for i in range(self.hossza)]
        self.utso:int = -1
        self.elso:int = self.utso
        
    def enforgas(self, data):
        
        if ((self.utso + 1) % self.hossza == self.elso):
            print('forgas is full')
            
        elif (self.elso == -1):
            self.elso = 0
            self.utso = 0
            self.forgas[self.utso] = data
        else:
            self.utso = (self.utso + 1) % self.hossza
            self.forgas[self.utso] = data
            
    def deforgas(self):
        if (self.elso == -1):
            print('forgas is empty')
            return 0
            
        elif(self.elso == self.utso):
            temp = self.forgas[self.elso]
            self.elso = -1
            self.utso = -1
            return temp
        else:
            temp = self.forgas[self.elso]
            self.elso = (self.elso + 1) % self.hossza
            return temp
        
if __name__ == '__main__':
    q = Forgo(6)
    q.enforgas(6)
    q.enforgas(5)
    for l in range(2):
        print(q.deforgas())