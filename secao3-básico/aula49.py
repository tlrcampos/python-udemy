'''

Lista em Python
Tipo List - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read, Update,   Delete
Criar, Ler, alterar, apagar = list[i] (CRUD)

'''
import os
os.system('cls')

lista = [10,20,30,40,50,60]
numero = lista[2]
print(lista[2], numero, sep=' - ')
lista[2] = 300
print(lista)
del lista[2]
print(lista[2], numero, sep=' - ')
lista.append(70)
lista.append(80)
lista.append(90)
print(lista)
lista.pop()
print(lista)
ultimo_valor_removido = lista.pop()
print("Valor removido pelo pop: ",ultimo_valor_removido)
print(lista)
valor_removido_por_indice = lista.pop(3)
print("Valor removido pelo indice no pop: ", valor_removido_por_indice)
print(lista)
