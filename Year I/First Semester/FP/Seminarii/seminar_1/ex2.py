import random
import math
lista_temperaturi = []
for ora in range(0,24):
    print("Temperatura pentru ora",ora, "este", end = " ")
    temp_curenta = random.uniform(10, 34)
    temp_curenta = round(temp_curenta, 1)
    print(temp_curenta)
    lista_temperaturi.append(temp_curenta)

#for i in range(len(lista_temperaturi)):
#    print('Ora', i, 'temperatura', lista_temperaturi[i])

for ora, temperatura in enumerate(lista_temperaturi):
    print('Ora', ora, 'temperatura', temperatura)

temp_minima = math.inf
ora_temp_minima = 0
for ora,temperatura in enumerate(lista_temperaturi):
    if(temp_minima > temperatura):
        temp_minima = temperatura
        ora_temp_minima = ora

print(temp_minima, ora_temp_minima)

medie = sum(lista_temperaturi)/len(lista_temperaturi)

temp_maxima = max(lista_temperaturi)

#https://stackoverflow.com/questions/364621/how-to-get-items-position-in-a-list
#incercare pentru aflare pozitie temperatura maxima in lista

zi = 'luni'

print(f"Temperatura medie in ziua de {zi} este:", medie)
print(f"Temperatura maxima in ziua de {zi} este:",temp_maxima)

#temp_min_direct = min
