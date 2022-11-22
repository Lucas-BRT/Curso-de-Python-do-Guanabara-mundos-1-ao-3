while True:
    num = int(input('DIGITE O NÚMERO QUE DESEJA SABER A TABUADA: '))
    if num < 0:
        print(f'PARANDO PROGRAMA...')
        break
    for n in range(1,10+1):
        print(f'{n} x {num} = {n*num}')















