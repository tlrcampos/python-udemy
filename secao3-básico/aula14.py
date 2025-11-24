a = 'AAAAAAA'
b = 'BBBBBBBBB'
c = 1.154524234
formato_1 = 'a={}'.format(a, b, c)
formato_2 = 'a={} b={}'.format(a, b, c)
formato_3 = 'a={} b={} c={}'.format(a, b, c)
formato_4 = 'a={} b={} c={:.4F}'.format(a, b, c)
formato_5 = 'a={0} b={1} c={2:.4F}'.format(a, b, c)
formato_6 = 'b={1} a={0} a={0} a={0} c={2:.2F}'.format(a, b, c)
formato_7 = 'a={nome2} b={nome3:.4f} c={nome1}'.format(nome1=a, nome2=b, nome3=c)


print(formato_1)
print(formato_2)
print(formato_3)
print(formato_4)
print(formato_5)
print(formato_6)
