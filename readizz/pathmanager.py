import pathlib
import constandvar as cv

path = []
path = cv.CurrPath.split("/")
#print(path)
path_len = len(path)
#print(path.pop(path_len-1))
cv.BackPath = cv.BackPath.join(path)
print(cv.BackPath)