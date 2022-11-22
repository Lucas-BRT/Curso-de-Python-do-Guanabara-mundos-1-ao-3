n = str(input('digite seu nome completo: '))

print(f'seu nome com todas as letras maiúsculas é: {n.upper()} ')
print(f'seu nome com todas as letras minusculas é: {n.lower()}')

a = len(n.replace(' ',''))



print(len(n))
print(f'seu nome possui {a} letras ')

b = n.split()

print(f'seu primeiro nome possui {len(b[0])} letras')


