continuar = True
maiores_de_18 = homens = mulheres_com_menos_de_20 = 0
while continuar:
    idade = int(input('DIGITE SUA IDADE: '))
    sexo = str(input('DIGITE SEU SEXO:[M/F] ')).upper().strip()[0]
    q = str(
        input('QUER CONTINUAR A CADASTRR PESSOAS?: [S/N] ')).upper().strip()[0]
    while q not in 'SN':
        q = str(
            input('QUER CONTINUAR A CADASTRR PESSOAS?: [S/N] ')).upper().strip()[0]
    if idade > 18:
        maiores_de_18 += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        if idade < 20:
            mulheres_com_menos_de_20 += 1
    if q == 'S':
        continuar = True
    elif q == 'N':
        continuar = False
print(f'''
EXISTEM {maiores_de_18} MAIORES DE 18 ANOS
EXISTEM {homens} HOMENS
EXISTEM {mulheres_com_menos_de_20} MULHERES COM MENOS DE 20
''')




















