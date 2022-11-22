total = 0
produtos_que_custam_mais_que_1000 = 0
produto_mais_barato = ''
preco_do_produto_mais_barato = 0
f = True
while True:
    nome = str(input('DIGITE O NOME DO PRODUTO: '))
    preco = float(input('DIGITE O PREÇO DO PRODUTO: '))
    total += preco
    if f:
        produto_mais_barato = nome
        preco_do_produto_mais_barato = preco
        f = False
    else:
        if preco < preco_do_produto_mais_barato:
            preco_do_produto_mais_barato = preco
            produto_mais_barato = nome
    if preco > 1000:
        produtos_que_custam_mais_que_1000 += 1
    continuar = input(
        'QUER CONTINUAR ADICONANDO PRODUTOS? [S/N]: ').upper().strip()[0]
    while continuar not in 'SN':
        continuar = input(
            'QUER CONTINUAR ADICONANDO PRODUTOS? DIGITE UM VALOR VALIDO! [S/N]: ').upper().strip()[0]
    if continuar == 'N':
        break
print(f'''
o total a se pagar é de {total}
{produtos_que_custam_mais_que_1000} custam mais de 1000 reais
o produto mais barato foi {produto_mais_barato}
''')
