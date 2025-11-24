'''
Iterando strings com while

'''

#       012345678910
nome = 'Luiz Otávio' # Iteráveis
#      11100987654321 

novo_nome = ''
indice = 0
tamanho = len(nome)
while indice < tamanho:
    letra = nome[indice]
    novo_nome += letra
    print(letra)
    indice += 1

print(novo_nome[::-1])