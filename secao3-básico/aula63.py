# Desempacotamento em chamadas
# de métodos e funções

import os
os.system('cls')

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

a, b, *_, ap, u = lista
print(a, u, ap)

for nome in lista:
    print(nome, end=' ', sep=' ')

print()
print(*lista)
print(*string)
print(*tupla)

salas = [
    ['Malas', 'Helena',],
    ['Elaine', ],
    ['Luiz', 'João', 'Eduarda', (0,10, 20, 30, 40)],
]

print(*salas, sep='\n', )