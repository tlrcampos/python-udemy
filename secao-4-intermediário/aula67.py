'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento(valor)
'''

import os
os.system('cls')

def soma(x, y):
    print(f'{x=}, {y=}','|',f'x + y = ',x + y)

soma(9, 4)  # argumentos não nomeados
soma(y=2, x=1) # argumentos nomeados
soma(22, y=1) # argumentos não nomeados && nomeados
