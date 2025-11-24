# Interpolação básica de strigs
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal(ABCDEF0123456789)

nome = 'Luiz'
preco = 1000.95897643
variavel = ' %s, o preço total foi R$ %.f ou de forma menos detalhada %.2f'  % (nome, preco, preco)
print(variavel)
print('O hexadecimal de %d é %x' % (15, 15))
print('O hexadecimal de %d é %x' % (3, 3))
print('O hexadecimal de %d é %x' % (7, 7))
print('O hexadecimal de %d é %x' % (10, 10))
print('O hexadecimal de %d é %04x' % (1500, 1500))
print('O hexadecimal de %d é %08X' % (1500, 1500))

