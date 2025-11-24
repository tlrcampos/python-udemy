'''
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será usado.
Refatorar: editar seu código.
'''

import os
os.system('cls')

def soma(x, y, t=100, z=None):
    if z is not None:
        print(f'z is not None.')
        print(f'x + y + t = ',x + y + t)
    else:
        print(f'z is None.')
        print(f'x + y = ',x + y)


soma(1, 2)
soma(21, 22)
soma(13, 22,z=33)

