import os

def getCpath(data:list, path:list):
    data = [map(str,l) for l in data]
    for l in data:
        print(str(data[l]))
        #var0 = ""
        #var0 = var0.join(data[l])
        #pathnext = os.path.join(path, data[l])
        #print(pathnext)
    #return pathnext
            

def itisafile(path=str):
    if os.path.isfile(path) == True:
        return True
    else:
        return False
    
def getSizesoffiles(path0):
    path = path0
    size_ls = []
    all_files = os.listdir(path)
    print(type(all_files))
    
    for l in range(len(all_files)):
        currPath = os.path.join(path, all_files[l])
        print(currPath)
        if itisafile(f"{path} + '/' + {all_files[l]}") == True:
            fuck = os.path.splitext(f"{path} + '/' + {all_files[l]}")
            print(fuck)
            print(f"{all_files[l]} - {round(os.path.getsize(currPath) / 1024, 2)} kb Extension {fuck[1]}")
            size_ls.append(round(os.path.getsize(f"{path} + '/' + {all_files[l]}") / 1024, 2))
        else:
            #print('directory')
            size_ls.append('directory')
    #print(str(size_ls))
    return size_ls

if __name__ == '__main__':
    getSizesoffiles("C:/Users/csehg/pytry")