'''

https://docs.python.org/pt-br/3/library/stdtypes.html
imutáveis que vimos: str, int, float, bool

'''

string = 'Luiz Otávio'
outra_variavel = string
outra_variavel_2 = f'{string[:3]}ABC{string[4:]}'
#string[3] = 'ABC'
print(string)
print(outra_variavel_2)
print(string.capitalize())
print(string.zfill(20))
