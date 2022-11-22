media = 0
maior = 0
menor = 0
numeros = 0
primeira = True
while True:
    num = int(input('numero: '))
    numeros += 1
    media += num
    if primeira:
        maior = num
        menor = num
        primeira = False
    elif maior < num:
        maior = num
    elif menor > num:
        menor = num
    k = str(input('gostaria de continuar a digitar? [S/N]: '))
    k = k in 'Ss'
    if not k:
        break
print(f'a media é de {media/numeros}')
print(f'o maior numero foi o de {maior}')
print(f'o menor numero foi o de {menor}')
