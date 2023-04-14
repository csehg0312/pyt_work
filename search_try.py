def binarisv02(lista:list, keresett_szoveg, bal, jobb):
    talalat_lista:list = []
    if bal >= jobb:
        return talalat_lista

    else:
       kozep = (bal + jobb) // 2 
       if keresett_szoveg in lista[kozep]:
           talalat_lista.append(lista[kozep])
           

       elif keresett_szoveg > lista[kozep]:
           #keresett_szoveg a jobb oldalon
           return binarisv02(lista, keresett_szoveg, kozep + 1, jobb)
       
       else:
           #keresett_szoveg a bal oldalon
           return binarisv02(lista, keresett_szoveg, bal, kozep - 1) 

# a keresesi algoritmus egy mar rendezett tombben kepes keresni egy keresett szoveg utan
def binaris_kereses(lista:list, keresett:str):
    left, right = 0, len(lista) - 1
    talat_lista:list = []
    
    while left <= right:
        mid = (left + right) // 2
        
        if keresett in lista[mid]:
            talat_lista.append(lista[mid])
            print(talat_lista)
            #return mid
        
        if lista[mid] < keresett:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

def lista_kereses(a_lista_melyben_keresek:list, keresett_szoveg:str):
    rendezett_tomb = sorted(a_lista_melyben_keresek)
    eredmeny = binaris_kereses(rendezett_tomb, keresett_szoveg)
    
    if eredmeny == -1:
        print(f"{keresett_szoveg} not found in list.")
    else:
        print(f"{keresett_szoveg} found at index {eredmeny} in list.")
