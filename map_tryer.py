st = 'MB'
x = st.strip()
print(x)

def hexer(val):
    
    return ord(val)

def binner(val0):
    
    return bin(val0)

y = map(hexer,x)
#print(list(y))

z = map(binner, y)
print(list(z))


#print(ord(st.split()))
