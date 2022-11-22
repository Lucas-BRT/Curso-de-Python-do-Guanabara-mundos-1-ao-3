speed = int(input('a quantos Km/h você estava? '))

if(speed > 80):
    multa = (speed - 80) * 7.00
    print(f'EXCESSO DE VELOCIDADE! você tomará uma multa de {multa :.2f} R$ ')


