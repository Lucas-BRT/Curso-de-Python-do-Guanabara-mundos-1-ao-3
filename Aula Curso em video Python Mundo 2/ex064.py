soma = 0
key = True
numeros = 0
while key:
    n = float(input('NUMERO: '))    
    if n == 999:
        break
    else:
        numeros += 1
        soma += n
print(f'\nvocê digitou {numeros} numeros\ne a soma de todos eles é {soma} ')


















































