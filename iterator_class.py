import os
from time import perf_counter

class TombIterator:
    def __init__(self, max):
        self.max = max
        
    def __iter__(self):
        self.e = 0
        return self
    def __next__(self):
        if self.e <= self.max:
            tmp = self.e
            self.e += 1
            return tmp
        else:
            raise StopIteration

utv = os.path.expanduser('~')
lista = os.listdir(utv)

start = perf_counter()

for i in range(len(lista)):
    ...


end = perf_counter()
print(f'Total time: {end - start}')


start = perf_counter()

classiter = TombIterator(len(lista))
itering = iter(classiter)
for x in itering:
    ...

end = perf_counter()
print(f'Total time: {end - start}')

