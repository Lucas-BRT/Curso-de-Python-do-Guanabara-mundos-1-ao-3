menores = 0
maiores = 0

for c in range(1, 8):
    a_sua_mae = int(input(f'DIGITE A IDADE DA PESSOA {c} '))

    if a_sua_mae <= 20:
        menores += 1
    elif a_sua_mae >= 21:
        maiores += 1


print(f''' 
MENORES {menores}
MAIORES {maiores}
''')















