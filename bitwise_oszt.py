def bitt_oszt(a,b):

    val = 0 # a valasz valtozoja

    haNeg = a < 0 or b < 0 # Meggyozodnunk kell hogy a szamok pozitivak legyenek

    a = abs(a) 
    b = abs(b) 

    for i in range(31,-1,-1): # a for loop inditasa

        if b << i <= a  : # megnezzuk hogy b a 2**i ra emelve nagyobb vagy egyenlo a-nal 
            a -= b << i   # kivonjuk b << i - et a-bol
            val += 1 << i # hozzaadjuk 2 emelt i-t a valaszhoz

    # ha az eredmeny nem negativ akkor visszaadhatjuk
    return val if haNeg == 0 else -1 * val

c = bit_div(20480,1023)
print(f'C is: {c}')