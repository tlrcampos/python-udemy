'''
Flag(bandeira) - Marcar um local
None = Não valor

is e is not = é ou não é(tipo, valor, identidade)
id = identidade de um elemento na memória

'''

v1 = 'a'
v2 = 'a'
v3 = 'b'

print(id(v1))
print(id(v2))
print(id(v3))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faça algo.")
else:
    print("Não faça algo.")

print(passou_no_if, passou_no_if is None, passou_no_if == None)
print(passou_no_if is not None)

if passou_no_if is None:
    print("Não passou no if.")
elif passou_no_if is not None:
    print("Passou no if.")