a = 0
contador = 0
for c in range(1+2, 500, 3):
    if c % 2 != 0:
        a += c
        contador += 1
print(f'A SOMA DOS VALORES É {a} \n A QUANTIDADE DE NÚMEROS É {contador}    ')
