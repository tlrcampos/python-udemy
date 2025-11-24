'''
enumerate - enumera iteráveis(índices)
'''


import os
os.system("cls")

lista = ["Sarinha ", "a diretora ", "do TRF 5ª região."]
lista.insert(2, "supimpa ")
print(lista)

texto = ""
for item in enumerate(lista):
    indice, nome = item
    texto = texto + nome
    print(item," | ", indice," - ", nome)

print(texto)

print()
for indice, nome in enumerate(lista):
    print(indice," - ", nome)


lista_enumerada = enumerate(lista)
lista_do_enumerator = list(lista_enumerada)
print()
print(lista_enumerada)
print(lista_do_enumerator)

#print(next(lista_enumerada), lista_enumerada)

print()
for str in lista_enumerada:
    print(str, type(str))

print()
print(lista_enumerada)
lista_do_enumerator = list(lista_enumerada)
print("Lista vem vazia pq o enumerator, que é um iterator, foi todo consumido. Resultado: ",lista_do_enumerator)
print()

print("FOR da tupla: ")
for tupla_enumerada in enumerate(lista):
    for valor in tupla_enumerada:
        print(f'\t{valor}')

print()