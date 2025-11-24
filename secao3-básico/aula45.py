'''

Iterável -> str, range, etc(__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador

'''

numeros = range(0, 100, 8)

for n in numeros:
    print(n)

texto = iter('Luiz')
print()
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())

texto_2 = iter('Thiago')
print()
print(next(texto_2))
print(next(texto_2))
print(next(texto_2))
print(next(texto_2))
print(next(texto_2))
print(next(texto_2))

# for letra in texto:
texto_3 = 'Isabella'      # iterável
iterador = iter(texto_3)  # iterador

print()
while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
