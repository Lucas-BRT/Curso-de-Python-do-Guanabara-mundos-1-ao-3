n = input('digite um número entre 0 e 9999: ')
n = int(n)

a = n // 1 % 10
b = n // 10 % 10
c = n // 100 % 10
d = n // 1000 % 10

print(f'o digito da unidade é: {a}')
print(f'o digito da dezena é: {b}')
print(f'o digito da centena é: {c}')
print(f'o digito dos milhares é: {d}')






