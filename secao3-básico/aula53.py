'''
for in com listas
'''
import os
os.system('cls')

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for nome in lista:
    print(nome, type(nome))

indices = range(len(lista))
print()
print(indices)
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

