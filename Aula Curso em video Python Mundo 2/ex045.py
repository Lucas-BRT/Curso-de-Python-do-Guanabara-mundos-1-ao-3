import random

print('''ESCOLHA ENTRE
    - PEDRA
    - PAPEL
    - TESOURA 
    ''')

while True:
    A = str(input())

    A = A.replace(' ', '')
    A = A[:2].lower()

    B = random.choice(['pe','pa','te'])

    if(A == 'pe'):
 

        if(B == 'pa'):
            print('você perdeu! eu escolhi PAPEL ')
            pass
        elif(B == A):
            print('empate! eu também escolhi PEDRA ')
            pass
        elif(B == 'te'):
            print('você ganhou! eu escolhi TESOURA ')
            pass

        pass
    elif(A == 'pa'):


        if(B == 'te'):
            print('você perdeu! eu escolhi TESOURA ')
            pass
        elif(B == A):
            print('empate! eu também escolhi PAPEL ')
            pass
        elif(B == 'pe'):
            print('você ganhou! eu escolhi PEDRA ')
            pass


        pass
    elif(A == 'te'):


        if(B == 'pe'):
            print('você perdeu! eu escolhi PEDRA ')
            pass
        elif(B == A):
            print('empate! eu também escolhi TESOURA ')
            pass
        elif(B == 'pa'):
            print('você ganhou! eu escolhi PAPEL ')
            pass


        pass
    else:
        print('DIGITE UM VALOR VÁLIDO')









print(A)



























