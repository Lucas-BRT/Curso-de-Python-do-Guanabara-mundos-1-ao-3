a = float(input('DIGITE O COMPRIMENTO DA PRIMEIRA RETA: '))
b = float(input('DIGITE O COMPRIMENTO DA SEGUNDA RETA: '))
c = float(input('DIGITE O COMPRIMENTO DA TERCEIRA RETA: '))

# equilatero
if(a == b == c):
    if((b - c < a < b + c)):
        print('EQUILÁTERO')
    else:
        print('triangulo não possível')

elif((a == b) or (b == c) or (c == a)):
    if((b - c < a < b + c)):
        print('ISÓCELES')
    else:
        print('triangulo não possível')
elif(a != b != c):
    if((b - c < a < b + c)):
        print('ESCALENO')
    else:
        print('triangulo não possível')








