''' while/else '''
string = 'Valor qualquer'

i= 0
tamanho = len(string)
while i < tamanho:
    letra = string[i]
    print(letra)
    i += 1
else:
    print('O else do while foi executado.')

print('Fora do 1º while.')
print()
i= 0
tamanho = len(string)
while i < tamanho:
    letra = string[i]
    print(letra)
    if letra is ' ':
        break
    i += 1
else:
    print('O else do while foi executado.')

print('Fora do 2º while.')