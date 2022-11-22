num = int(input('DIGITE UM NÚMERO: '))
raz = int(input('DIGITE UMA RAZÂO: '))
a = 1
b = 10
while a <= b:
    print(f'O {a}ª numero é {num} ')
    num += raz
    if a == b:
        n = int(input('QUANTOS NUMEROS A MAIS VOCÊ GOSTARIA DE VER?'))
        if n <= 0:
            break
        else:
            b += n
    a += 1
















