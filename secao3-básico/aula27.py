'''
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p][::]
Obs.: a função len retorna a qtd
de caracteres da str
'''

variavel = 'Olá mundo novo'
print(variavel[5])
print(variavel[-4])
print(variavel[4:])
print(variavel[4:8])
print(variavel[2:5])
print(variavel[0:5])
print(variavel[-8:-2])
print(variavel[-5:])
print(variavel[:-3])
print(len(variavel[4:7]))
print(variavel[0:len(variavel):1])
print(variavel[0:len(variavel):2])
print(variavel[0:len(variavel):3])
print(variavel[0:len(variavel):4])
print(variavel[::-1])
print(variavel[-1:-15:-1])
