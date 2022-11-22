numero = int(input('DIGITE UM NÚMERO: '))
x = 0
for contador in range(1, numero+1):
    if(numero % contador == 0):
        x += 1
if(x == 2):
    print('O NÚMERO É PRIMO!!!')
else:
    print('O NÚMERO NÃO É PRIMO!!!')

        






