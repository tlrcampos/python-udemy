'''
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros(argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None(nada).
'''

import os
os.system('cls')

def imprimir():
    print('Várias')
    print('Várias')
    print('Várias')
    print('Várias')

def imprimir2(a, b, c):
    print(f'{a}')
    print(f'{b}')
    print(f'{c}')


imprimir()
imprimir2(1,2,3)
imprimir()
imprimir2(1,2,3)
imprimir()