def este_prim(nr):
    if nr <= 1 :
        return 0
    if nr % 2 == 0:
        return 0
    if nr == 2 :
        return 1
    for divizor in range(3,nr,2) :
        if nr % divizor == 0 :
            return 0
    return 1

n=1
exista = False
numar = int(input("Introduceti numarul:"))
for prim1 in range(1,numar//2):
    if este_prim(prim1) == 1 :
        for prim2 in range(prim1,numar) :
            if este_prim(prim2) == 1 :
                if prim1 + prim2 == numar :
                    primul_numar_prim = prim1
                    al_doilea_numar_prim = prim2
                    exista = True
                elif prim1 + prim2 > numar :
                    break
    if exista == True :
        break
if exista == False :
    print("Nu exista o suma de numere prime egala cu", numar)
else:
    print(numar, '=', primul_numar_prim, '+',al_doilea_numar_prim)