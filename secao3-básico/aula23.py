# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = true

senha = input('Senha: ')

if not senha :          # senha não vazia
    print('Entrou')
else:
    print('Senha incorreta')

print(not True)
print(not False)
print(not 1)
print(not 0)