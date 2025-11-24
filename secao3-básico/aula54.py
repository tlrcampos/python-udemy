'''

Introdução ao desempacotamento + tuples(tuplas)

'''

import os
os.system('cls')

lista = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = lista

print(nome1, nome2, nome3)

nome1, nome2, nome3, nome4 = ["Thiago", "Leite", "Ribeiro", "Campos"]
print(nome1, nome2, nome3, nome4)

nome1, *sub_lista = ["Thiago", "Leite", "Ribeiro", "Campos"]
print(nome1, sub_lista)

nome1, nome2, nome3, nome4, *resto = ["Thiago", "Leite", "Ribeiro", "Campos"]
print(nome1, nome2, nome3, nome4, resto)
