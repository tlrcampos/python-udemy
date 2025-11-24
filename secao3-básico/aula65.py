'''
CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10

EX: 746.824.890-70(746824890)

  10 9  8  7  6  5  4  3  2 
   7 4  6  8  2  4  8  9  0
  70 36 48 56 12 20 32 27 0

  11 10  9  8  7  6  5  4 3  2
  7   4  6  8  2  4  8  9 0  7  <-- PRIMEIRO DÍGITO
  77 40 54 64 14 24 40 36 0 14

 Somar todos os resultados(10):
 70+36+48+56+12+20+32+27+0=301
 Somar todos os resultados(11):
 77+40+54+64+14+24+40+36+0+14=363
 
 Multiplicar o resultado anterior por 10
 301 * 10 = 3010
 Obter o resto da divisão da conta anterior por 11
 3010 % 11 = 7
 Se o resultado anterior for maior que  9:
    resultado é 0
 Contrário disso:
    resultado é o valor da conta

 O primeiro digito do CPF é 7

 Multiplicar o resultado anterior por 10
 363 * 11 = 3630
 Obter o resto da divisão da conta anterior por 11
 3630 % 11 = 0
 Se o resultado anterior for maior que  9:
    resultado é 0
 Contrário disso:
    resultado é o valor da conta

 O segundo digito do CPF é 0
 
'''

import os , re
os.system('cls')

#cpf_enviado_usuario = '7468248970'
#cpf_enviado_usuario = '746.824.890-70'.replace('.', '').replace(' ', '').replace('-', "")
entrada = input('CPF padrão [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = cpf_enviado_usuario[:9] + str(digito_1)

resultado_digito_2 = 0
contador_regressivo_2 = 11
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

usuario_invalido_total_11 = cpf_enviado_usuario.count(cpf_enviado_usuario[1]) == 11

if cpf_gerado_pelo_calculo == cpf_enviado_usuario and usuario_invalido_total_11 == False:
    print(f'{cpf_enviado_usuario} é válido!')
elif cpf_gerado_pelo_calculo == cpf_enviado_usuario and usuario_invalido_total_11 == True:
    print('CPF inválido. Todos os caracteres estão repetidos.')
else:
    print('CPF inválido!')
