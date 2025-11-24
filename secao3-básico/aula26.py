'''
s - string
d - int
f - float

.<número de dígitos>f
x ou X - Hexadecimal
(Caracter)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - força o número aparecer antes dos zeros
Sinal - + ou -
Ex: 0>-100, 1f
Conversiont flags - !r !s !a __repr__ 

'''
variavel = 'ABC'
print(f'{variavel}')
print(f'.{variavel:>10}')
print(f'{variavel:<10}.')
print(f'.{variavel:^10}.')
print(f'.{variavel:$^10}.')
print(f'{1000.36483843248:,.1f}')
print(f'{600-1000.36483843248:-,.1f}')
print(f'{1000.36483843248:+,.1f}')
print(f'{1000.36483843248:0>10.1f}')
print(f'{1000.36483843248:0<10.1f}')
print(f'{1000.36483843248:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
print(f'{variavel!s}')
print(f'{variavel!a}')
