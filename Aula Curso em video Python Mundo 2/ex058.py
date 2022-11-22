import random
num = random.randint(0,10)
tentativas = 0
k = True
while k:
    chute = int(input('CHUTE UM NÚMERO ENTRE 0 E 10: '))
    tentativas += 1
    if chute == num:
        k = False  
        print(f'VOCÊ ACERTOU!!! EU PENSEI EM {num} ')
        print(f'VOCÊ SÓ PRECISOU DE {tentativas} TENTATIVAS! ')
    else:
        print(f'VOCÊ ERROU! EU NÃO PENSEI EM {chute}! TENTE NOVAMENTE ')














