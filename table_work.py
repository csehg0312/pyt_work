import os

path = "C:/Users/csehg/pywork/bcpywork/data"

def create_table(arg):
    path = arg
    fejlec = {'Name':[], 'Size':[], 'Lastly used':[]}
    direx = os.listdir(path)
    try:
        fejlec.update({'Name':[direx]})
    except SystaxError:
        print(f'{fejlec} is not updatable')
    print(str(fejlec))
    return fejlec

if __name__ == '__main__':
    create_table(path)
    