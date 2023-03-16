import os
import asyncio
from collections import deque
from dataclass_file import File
from dataclass_folder import Folder

# def sorted_data(ut:str):
#     text_file_list = ['.txt','.rtf','.log', '.doc','.docx']
#     music_file_list = ['.mp3', '.mp4','.ma4','.flac','.wav','.wma']
#     pic_file_list = ['.jpg','.png','.tiff','.pdf','.gif', '.raw']
#     exec_file_list = ['.exe', '.msi']
#     zipped_file_list = ['.zip', '.7zip']
#     video_file_list = ['.mp4','.mov']
# 
#     #path = 'C:/Users/csehg/Documents'
#     filebase = {}
# 
#     def istxt(file:str):
#         _,comp = os.path.splitext(file)
#         if comp.lower() in text_file_list:
#             return 1
#         elif comp.lower() in music_file_list:
#             return 2
#         elif comp.lower() in pic_file_list:
#             return 3
#         elif comp.lower() in video_file_list:
#             return 4
#         elif comp.lower() in exec_file_list:
#             return 5
#         elif comp.lower() in zipped_file_list:
#             return 6
#         else:
#             return 0
#         
#     def getsize(path):
#         
#         return os.path.getsize(path)
# 
#     def getlasttime(path):
#         return os.path.getctime(path)
# 
# 
#         
# 
#     filebase.update({'Path':path})
#     parent, _ = os.path.split(path)
#     filebase.update({'Parent':parent})
#     print(filebase.values())
#     filebase.update({'Folders': deque([x for x in os.listdir(path) if os.path.isdir(os.path.join(path,x))])})
#     print(filebase.values())
#     print(sys.getsizeof(filebase))
#     # filebase.update({'Text Files:': [x for x in os.listdir(path) if istxt(x)]})
#     #filebase.update({'Files': deque([x for x in os.listdir(path) if os.path.isdir(os.path.join(path,x)) == False])})
#     # print(filebase.values())
#     # print(sys.getsizeof(filebase))
#     filebase.update({'Else': deque([x for x in os.listdir(path) if istxt(x) == 0 and x not in filebase.get('Folders')])})
#     filebase.update({'Text': deque([x for x in os.listdir(path) if istxt(x) == 1])})
#     filebase.update({'Music': deque([x for x in os.listdir(path) if istxt(x) == 2])})
#     filebase.update({'Photo': deque([x for x in os.listdir(path) if istxt(x) == 3])})
#     filebase.update({'Video': deque([x for x in os.listdir(path) if istxt(x) == 4])})
#     filebase.update({'Executables': deque([x for x in os.listdir(path) if istxt(x) == 5])})
#     filebase.update({'Zipped': deque([x for x in os.listdir(path) if istxt(x) == 6])})
#     print(filebase.items())
#

def simple_data(ut):
    try:
        filebase:dict
        filebase = {'Path':str, 'Parent':str, "Folders":deque([]), "Files":deque([])}

        filebase.update({'Path':ut})
        parent:str
        parent, _ = os.path.split(ut)
        filebase.update({'Parent':parent})
        #print(filebase.values())
        filebase.update({"Folders": deque([x for x in os.listdir(ut) if os.path.isdir(os.path.join(ut,x))])})
        filebase.update({"Files": deque([x for x in os.listdir(ut) if os.path.isdir(os.path.join(ut,x)) == False and os.path.ismount(os.path.join(ut,x)) == False])})
        #filebase.update({"FilePath": deque([os.path.join(ut,x) for x in filebase.get('Files')])})
        #print(filebase.values())
        return filebase
    except (OSError, PermissionError):
        return {}

def mappa_osztaly(ut:str):
    bazis:dict
    bazis = {}
    mappa:deque
    mappa = deque([])
    bazis=simple_data(ut)
    mappa = bazis.get('Folders')
    sor:deque
    sor = deque([Folder(ut,x) for x in mappa])
    bazis.clear()
    return sor


def fajl_osztaly(ut:str):
    base:dict
    base = {}
    fajls:deque
    fajls = deque([])
    base = simple_data(ut)
    fajls = base.get('Files')
    sor:deque
    sor = deque([File(ut, x) for x in fajls])
    base.clear()
    return sor

def get_data_from_file(obj:File):
    ob: File = obj
    return [ob.nev.default_factory, ob.bovitmeny.default_factory, ob.modositdate.default_factory, ob.meret.default_factory]

def get_data_folder(obj:Folder):
    ob: Folder = obj
    return[ob.mappa, ob.megnevez.default_factory, ob.modisitasdate.default_factory, 0]


def create_twoD_list(ut:str):
    hossz:int = len(os.listdir(ut))
    
    mappaobj:deque = deque([])
    mappaobj = mappa_osztaly(ut)
    mappaMap = map(get_data_folder, mappaobj)
    
    

    fajlobj:deque = deque([])
    fajlobj = fajl_osztaly(ut)
    fajlMap = map(get_data_from_file, fajlobj)
    
    mappaMap = list(mappaMap)
    fajlMap = list(fajlMap)
    print(type(mappaMap))
    print(type(fajlMap))
    
    mappasor = deque([x for x in mappaMap])
    fajlsor = deque([x for x in fajlMap])
    tomb:list = []*hossz
    for m in mappasor:
        tomb.append(m)
        
    for f in fajlsor:
        tomb.append(f)
    
    return tomb

    
if __name__ == '__main__':
    utv = os.getcwd()
    create_twoD_list(utv)
#     S = mappa_osztaly(utv)
#     print(S)
#     print(sys.getsizeof(S))


