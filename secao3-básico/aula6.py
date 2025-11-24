# converção de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos mutáveis e primitivos:
# str, int, float, bool

print(1 + 1)
# print('1' + 1) =>> Da o seguinte erro:  "c:\workspace-udemy\projeto-python-3-completo\aula6.py",
#  line 8, in <module> print('1' + 1)
print('a' + 'b')
print(int('1543'), type('1'))
print('1' + str(1))
print(1 + int('1'))
print(1.2 + float('1.31'))
print(type(1.2 + float('1.31')))
print(bool(' '))
print(bool(''))
print(str(11) + 'b')