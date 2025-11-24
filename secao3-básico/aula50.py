'''

Listas em Python
Tipo List - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis
    append - adiciona um item ao final
    insert - adiciona um item no índice escolhido
    pop - remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + -  concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD) 

'''

import os
os.system('cls')

#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
print(lista)
lista.pop()
print(lista)
lista.append('Luiz')
print(lista)
del lista[-1]
print(lista)
lista.insert(0,5)
print(lista)
lista.insert(50, 34) # coloca no (último índice + 1)
print(lista[5])
lista.clear()
print(lista)



