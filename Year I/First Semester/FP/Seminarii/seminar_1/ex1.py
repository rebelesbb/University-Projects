n = int(input("Introduceti numarul: "))
nr_cifre = 0

#suma cifre impare

suma = 0

while n != 0:
    if n%10 == 1:
        suma+=(n%10)
    n/=10

print(suma)
    


#numar cifre
if n == 0 :
    nr_cifre = 1
else:
    while n != 0 :
        nr_cifre+=1
        n//=10

#print(nr_cifre)




