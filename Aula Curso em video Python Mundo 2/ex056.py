media = 0
idade_do_homem_mais_velho = 0
mulheres_menores_de_20 = 0
for c in range(1, 5):
    nome = str(input('DIGITE SEU NOME: '))
    idade = int(input('DIGITE SUA IDADE: '))
    sexo = str(input('DIGITE SEU SEXO: '))
    if sexo == 'm':
        if idade > idade_do_homem_mais_velho:
            nome_do_homem_mais_velho = nome
    elif sexo == 'f':
        if idade < 20:
            mulheres_menores_de_20 += 1
    media += idade
print(f'''     

A MÉDIA DE IDADE É DE {media/c}
O HOMEM MAIS VELHO É {nome_do_homem_mais_velho}
EXISTEM {mulheres_menores_de_20} MULHERES COM IDADE MENOR A 20 ANOS

''')
