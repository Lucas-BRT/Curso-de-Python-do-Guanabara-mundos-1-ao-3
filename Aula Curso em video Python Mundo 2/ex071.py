import tkinter








saque = int(input('digite um valor inteiro para sacar: '))
notas_de_50 = saque // 50
resto = saque % 50
print(f'{notas_de_50} notas de 50 ')
notas_de_20 = resto // 20
resto = saque % 20
print(f'{notas_de_20} notas_de_20')
notas_de_10 = resto // 10
resto = saque % 10
print(f'{notas_de_10} notas_de_10')
notas_de_1 = resto // 1
resto = saque % 1
print(f'{notas_de_1} notas_de_1')














