''' Calculadora com while '''

while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador(+-*/): ')
    numero_float_1 = 0.0
    numero_float_2 = 0.0
    numeros_validos = None

    try:
        numero_float_1 = float(numero_1)
        numero_float_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    #Início - Cálculos
    print('Realizando sua conta. Confira o resultado abaixo: ')
    if operador == '+':
        print(numero_float_1 + numero_float_2)
    elif operador == '-':
        print(numero_float_1 - numero_float_2)
    elif operador == '/':
        print(numero_float_1 / numero_float_2)
    elif operador == '*':
        print(numero_float_1 * numero_float_2)
    else:
        print('Nunca deveria chegar aqui.')
    #Fim - Cálculos

    sair = input('Quer sair? [s]im.')
    sair = sair.lower()
    sair = sair.startswith('s')

    if sair is True:
        break

