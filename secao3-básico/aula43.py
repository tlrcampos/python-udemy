#Usamos o while quando não sabemos o número de repetições que vamos ter.

texto = 'Python'

i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(i," - ",texto[i])
    i += 1

# Usando o for

print()
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')