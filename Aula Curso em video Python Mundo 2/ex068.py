from random import randint
vitorias = 0
while True:
    print('-=-'*30)
    player = int(input('DIGITE UM NÚMERO: '))
    pc = int(randint(1,1001))
    escolha = str(input('ESCOLHA ENTRE IMPAR OU PAR: ')).strip().upper()
    while escolha[0] not in 'IP':
        escolha = str(input('ESCOLHA ENTRE IMPAR OU PAR: ')).strip().upper()
    result = None
    if (player + pc) % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    if result[0] == escolha[0]:
        print(f'PARABÉNS, VOCÊ ESCOLHEU {escolha} E ACERTOU! {player + pc} é {result}')
        vitorias +=1
    else:
        if vitorias > 1:
            perda = f'VOCê ACERTOU {vitorias} VEZES MAS AGORA PERDEU PORRA!' 
        else:
            perda = ''
        print(f'PERDEU FILHO DA PUTA! {perda}')










