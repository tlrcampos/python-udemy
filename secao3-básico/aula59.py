'''
split e join com list e str
split - divide uma string 
join - une uma string
'''

import os
os.system('cls')

frase = 'Olha só que, coisa interessante.'

lista_palavras = frase.split()
print(lista_palavras)

lista_palavras2 = frase.split(',')
print(lista_palavras2)