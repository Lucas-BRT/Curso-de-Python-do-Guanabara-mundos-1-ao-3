a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if(( c < a + b ) and ( b < a + c ) and (a  < b + c ) ):
    print('Triangulo')
else:
    print('Não Triangulo')








