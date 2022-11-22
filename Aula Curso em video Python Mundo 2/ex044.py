v = float(input('DIGITE O VALOR DO PRODUTO: '))
p = int(
    input('''
ESCOLHA O METODO DE PAGAMENTO 
1 - A VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
2 - A VISTA NO CARTÃO: 5% DE DESCONTO
3 - ATÉ 2X NO CARTÃO: PREÇO NORMAL
4 - 3X OU MAIS NO CARTÃO: 20% DE JUROS
'''))

if p == 1:
    print(f'\n A VISTA O PRODUTO FICA POR {v * 0.9} R$ ')
elif p == 2:
    print(f'\n A VISTA NO CARTÃO O PRODUTO FICA POR {v * 0.95} R$ ')
elif p == 3:
    print(f'\n EM ATÉ 2X NO CARTÃO O PRODUTO FICA POR {v} R$ ')
elif p == 4:
    parcelas = int(input('quantidade de parcelas: '))

    if(parcelas >= 3):
        v *= 1.20
        v_parcelas = v / parcelas

        print(
            f'\n EM {parcelas} NO CARTÃO O PRODUTO FICA POR {parcelas} VEZES DE {v_parcelas} R$ PARA UM TOTAL DE {v} R$ '
        )
    else:
        print('DIGITE UM VALOR VÁLIDO DE PARCELAS')
