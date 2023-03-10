from random import randrange
from collections import deque

def createRand:
    ls:deque = deque([])

    for i in range(10):
        ls.append(randrange(1,10))
    return ls

# print(type(ls))
# print(ls)

#itt jon a gyorsrendezes
#oszd meg es uralkodj modszer rekurziv algoritmus + randomizalas
#Monte Carlo algoritmusok --> mindig gyors es nagyon ritkan hibas algoritmus
#Las Vegas algoritmusok --> mindig helyes eredmeny es nagyon ritkan lassu PL: gyorsrendezes

def particioner():
    ...

def quickSort():
    ...