import os
from collections import deque
from time import perf_counter

#map (use iterable[list, set, string, dictionary], and it uses all the data to a function)
#lambda function is a one line function that specifies a data for a given

path = 'C:/Users/csehg/pytry'
lst = ['file_manager.py', 'dataclass_drive.py', 'event_handler.py']

def getsize(path):
    return os.path.getsize(path)
start = perf_counter()
#sl = [x for x in lst map(lambda x: path + '/' + x, getsize)]
pl = list(map(lambda x: path + '/' + x,lst))
sl = list(map(getsize, pl))
end = perf_counter()

print(f'{end - start}')

st = deque(['file_manager.py', 'dataclass_drive.py', 'event_handler.py'])

start = perf_counter()
P = deque([map(lambda x: path + '/' + x,st)])
S = map(getsize, P)

end = perf_counter()

print(f'{end - start}')
