house_price = int(input('QUAL É O VALOR DA CASA QUE VOCÊ QUER FINANCIAR? '))
years = int(input('EM QUANTOS ANOS VOCÊ QUER FINANCIAR ESSA CASA? '))
wage = int(input('QUAL É O SEU SALÁRIO MENSAL? '))

parcelas = house_price / (years * 12)


if(parcelas <= (wage * 0.3)):
    print(
        f' VOCÊ PODE FINANCIAR ESSA CASA EM {years} ANOS POR {parcelas} R$ POR MÊS ')
else:
    print(
        f'INFELISMENTE NÃO PODEMOS ACEITAR SEU PEDIDO DE FINANCIAMENTO PARA ESSA CASA POIS AS PARCELAS DE {parcelas:.2f} ULTRAPÁSSAM 30% DO SEU SALÁRIO MENSAL DE {wage} ')

print('\n')






