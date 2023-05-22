from winshell import recycle_bin, recent, shortcut, sys, personal_folder, desktop, favourites
from os.path import commonpath

#print(recycle_bin().enumerate())
pth = "C:\\Users\\csehg\\AppData\\Roaming\\Microsoft\\Windows\\Recent\\table_listed04.lnk"
p = "C:\\Users\\csehg\\AppData\\Roaming\\Microsoft\\Windows\\Recent\\nice.lnk"
#p = p.replace("\", "\\")

ls = [i for i in recycle_bin().enumerate()]
print(ls)
print(recent())
#------------------------
real_pth = shortcut(p)
print(type(real_pth))
print(real_pth.path)
#-----------------------

print(personal_folder())