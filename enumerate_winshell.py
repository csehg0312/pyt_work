from winshell import recycle_bin

#print(recycle_bin().enumerate())

ls = [i for i in recycle_bin().enumerate()]
print(ls)