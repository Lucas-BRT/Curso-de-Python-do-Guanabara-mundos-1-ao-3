n1 = float(input('DIGITE SUA PRIMEIRA NOTA: '))
n2 = float(input('DIGITE SUA SEGUNDA NOTA: '))

n = (n1 + n2) / 2

if n < 5:
    print('REPROVADO')
    pass
elif n >= 5 and n <= 6.9:
    print('RECUPERAÇÃO')
    pass
else:
    print('APROVADO')
    pass





