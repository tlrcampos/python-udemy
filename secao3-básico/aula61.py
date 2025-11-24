'''
Lista de listas e seus índices
'''

import os
os.system('cls')

salas = [
    ['Malas', 'Helena',],
    ['Elaine', ],
    ['Luiz', 'João', 'Eduarda', (0,10, 20, 30, 40)],
]

print(salas)
print(salas[0][1])
print(salas[1][0])
print(salas[2][2])
print(salas[2][3])

print()
for sala in salas:
    print(sala)

print()
for sala in salas:
    for aluno in sala:
        print(aluno)
