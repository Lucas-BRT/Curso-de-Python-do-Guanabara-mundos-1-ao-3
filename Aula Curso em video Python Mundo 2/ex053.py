frase = str(input('DIGITE UMA FRASE: '))
frase_sem_espacos = frase.replace(' ', '')
tamanho_da_frase = len(frase_sem_espacos) - 1
letras_iguais = 0


for contador in range(0, tamanho_da_frase+1):

    contador_inverso = tamanho_da_frase - contador
    letra_a = frase_sem_espacos[contador]
    letra_b = frase_sem_espacos[contador_inverso]

    if(letra_a == letra_b):
        letras_iguais += 1


if(letras_iguais == tamanho_da_frase+1):
    print('É UM PALINDROMO')
else:
    print('NÃO É UM PALINDROMO SEU ARROMBADO DO CARALHO COMI A TUA MÃE')













