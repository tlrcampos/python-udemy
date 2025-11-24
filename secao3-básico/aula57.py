'''
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
não permita que o programa quebre com 
erros de índices inexistentes na lista.
'''

import os
os.system('cls')

lista = []
while True:

    print("Selecione uma opção: ")
    opcao = input("[i]nserir, [a]pagar, [l]istar: ")

    if opcao == 'i':

        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        
        indice_str = input('Escolha o índice a apagar da lista: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except :
            print('Não foi possível apagar esse índice: ', indice)

    elif opcao == 'l':

        os.system('cls')
        if len(lista) == 0:
            print("Nada para listar.")
        
        for i, valor in enumerate(lista):
            print(i, valor)

    elif opcao == 's':
        os.system('esc')