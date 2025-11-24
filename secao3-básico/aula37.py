'''
Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

'''

contador = 0

while contador < 100:
    contador += 1
    if contador % 3 != 0 and contador % 2 != 0:
        print(contador)
        continue

    if contador == 50:
        break
        

print('Não mostrou múltiplo de 3 e de 2!')