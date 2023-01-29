from dataclass_queue import Forgo
import os
import time
from collections import deque


path = 'C:/Users/csehg/Documents'
L = len(os.listdir(path))
use = os.listdir(path)

start = time.perf_counter()

gen = Forgo(L)
for l in range(L):
    gen.enforgas(use[l])
for _ in range(L):
    
    _ = gen.deforgas()
    
end = time.perf_counter()
spent = end - start

print(f'Time spent: {spent}')
print('============================================')

start = time.perf_counter()

pth_list = []*L

for j in range(L):
    pth_list.append(use[j])
    
for _ in range(L):
    _ = pth_list.pop()
    
end = time.perf_counter()

spen = end - start
print(f'Operation made in: {spen}')
print('============================================')

start = time.perf_counter()
deq = deque([])

for k in range(L):
#     deq.appendleft(use[abs(k-L+1)])
    deq.append(use[k])
    
#print(list(deq))
    
for _ in range(L):
    _ = deq.pop()
    
end = time.perf_counter()

sp = end - start
print(f'Operation made in: {sp} ')
    


