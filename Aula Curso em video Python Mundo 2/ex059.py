k = True
while k == True:
    n1 = float(input('DIGITE O PRIMEIRO NÚMERO: '))
    n2 = float(input('DIGITE O SEGUNDO NÚMERO: '))
    opcao = int(input(
        '\nO QUE VOCÊ QUER FAZER COM O NÚMERO? \n[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA\n'))
    if opcao == 1:
        soma = n1+n2
        print(f'\nA SOMA ENTRE {n1} E {n2} É {soma}! ')
    elif opcao == 2:
        multi = n1*n2 
        print(f'\nA MULTIPLICAÇÂO ENTRE {n1} E {n2} É {multi}! ')
    elif opcao == 3:
        array = []
        array.extend([n1,n2])
        array.sort()
        resposta = array[-1]
        if n1 == n2:
            resposta == 'NENHUM'
        print(f'O MAIOR NUMERO ENTRE {n1} E {n2} É {resposta}! ')
    elif opcao == 4:
        pass    
    elif opcao == 5:
        break
    






