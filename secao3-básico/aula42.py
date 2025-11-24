frase = 'O Python é uma linguagem de programação '\
'multiparadigma. '\
'Python foi criado por Guido Van Rossum.'

i = 0
qtde_que_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''
tamanho = len(frase)
letra_atual = ''
while i < tamanho:
    if frase[i] != ' ':
        letra_atual = frase[i]
        quantas_vezes_a_letra_apareceu = frase.count(letra_atual)

    if qtde_que_apareceu_mais_vezes < quantas_vezes_a_letra_apareceu and letra_atual != ' ':
        letra_que_apareceu_mais_vezes = letra_atual
        qtde_que_apareceu_mais_vezes = quantas_vezes_a_letra_apareceu

    print(letra_atual, quantas_vezes_a_letra_apareceu)
    i += 1

print()
print(f'Letra que apareceu mais vezes foi o \"{letra_que_apareceu_mais_vezes}\" que apareceu mais vezes {qtde_que_apareceu_mais_vezes}x')

