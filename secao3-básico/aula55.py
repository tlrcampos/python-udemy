'''

Introdução ao desempacotamento + tuples(tuplas)
|Tipo tupla >> uma lista imutável.

'''
import os
os.system("cls")

# Primeira forma de fazer uma tupla
nomes = "Thiago", "Leite", "Ribeiro", "Campos"
# Segunda forma de fazer uma tupla
nomes2 = ('Maria', 'Helena', 'Luiz')
# Esse código lança exceção pq é uma tupla e não permite alteração da tupla.
# nome[1] = "Ricardo"
# Terceira forma de fazer uma tupla
tup = ("Sarinha ", "a diretora ", "do TRF 5ª")
nomes3 = tuple(tup)

print(nomes)
nome1, *sub_lista = nomes
print(nome1, sub_lista)
print(nomes2)
print(nomes3)
