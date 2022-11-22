peso = float(input('DIGITE SEU PESO EM KG: '))
altura = float(input('DIGITE SUA ALTURA EM CENTIMETROS: '))
altura = altura
IMC = (peso / (altura * altura))
if (IMC < 18.5):
    print('ABAIXO DO PESO')
elif (IMC > 18.5 and IMC < 25):
    print('PESO NORMAL')
elif (IMC > 25 and IMC < 30):
    print('SOBRE PESO')
elif (IMC > 30 and IMC < 40):
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
