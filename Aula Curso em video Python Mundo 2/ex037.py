n = int(input('DIGITE UM NÚMERO: '))

op = int(input('''DIGITE 1 PARA CONVERSÃO PARA BINÁRIO\nDIGITE 2 PARA CONVERSÃO OCTAL\nDIGITE 3 PARA CONVERSÃO HEXADECIMAL\n: '''))

if op == 1:
    n = bin(n)
elif op == 2:
    n = oct(n)
elif op == 3:
    n = hex(n)
else:
    n = 'ERRO!!! SELECIONE UMA OPERAÇÂO VÁLIDA. '

print(f'O RESULTADO É {n} ')





