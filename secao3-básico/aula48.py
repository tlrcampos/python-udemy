'''

Listas em Python
Tipo List - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, + 

'''

import os
os.system('cls') # >> limpa o console

#      01234
#     -54321

string = 'ABCDE'  #5 carecteres
list_1 = list()
list_2 = []

print(list_1, list_2, type(list_1), type(list_2))
print(bool(list_1))
#índice    0     1          2         3      4    5
#índice   -6    -5         -4        -3     -2    1 
list_3 = [123, True, 'Luiz Otávio', list_1, 1.3, []]
print(list_3)
print(list_3[2], type(list_3[2]))
list_3[-4] = 'Maria'
print(list_3)
print(list_3[-4])