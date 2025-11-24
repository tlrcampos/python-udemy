'''
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/3/tutorial/floatingpoint.html
'''
import os, decimal
os.system('cls')

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2 
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 1))
print(round(numero_3, 2))

numero_3 = decimal.Decimal(0.1)
numero_4 = decimal.Decimal(0.7)
numero_5 = numero_3 + numero_4
print()
print(numero_5)
print(f'{numero_5:.2f}')
print(round(numero_5, 1))
print(round(numero_5, 2))

numero_6 = decimal.Decimal('0.1')
numero_7 = decimal.Decimal('0.7')
numero_8 = numero_6 + numero_7
print()
print(numero_8)
print(f'{numero_8:.2f}')
print(round(numero_8, 1))
print(round(numero_8, 2))
