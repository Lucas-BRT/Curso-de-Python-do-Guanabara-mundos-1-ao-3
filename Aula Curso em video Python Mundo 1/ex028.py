import random as rm

numero = rm.randrange(6)

chute = int(input('duvido adivinhar o número que eu estou pensando de 0 a 5! '))

if(chute == numero):
    print(f'droga! você acertou, eu estava pensando em {numero}!')
else:
    print(f'você errou! eu estava pensando em {numero}! ')


