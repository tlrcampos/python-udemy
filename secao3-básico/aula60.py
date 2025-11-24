'''
split e join com list e str
split - divide uma string
join - une uma string
'''
import os
os.system('cls')

frase = 'Olha, só ,que, coisa, interessante.'
lista_frase = frase.split(',')
print(lista_frase)

print()
for i, frase in enumerate(lista_frase):
    print(lista_frase[i].strip())

frases_unidas = "-".join(' abc ABC')
print()
print(frases_unidas)