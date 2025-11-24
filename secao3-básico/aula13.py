nome = 'Luiz Otávio'
altura = 1111.8
peso = 95
imc = peso / (altura * altura)

#f-strings
linha_1 = f'{nome} tem {altura:,.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.6f}'

print(linha_1)
print(linha_2)
print(linha_3)