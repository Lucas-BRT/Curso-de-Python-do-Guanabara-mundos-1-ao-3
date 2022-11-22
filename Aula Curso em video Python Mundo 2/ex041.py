from datetime import date

ano = date.today().year



print(ano)

y = int(input('DIGITE O ANO DE NASCIMENTO: '))

y = ano - y

print(y)
if (y <= 9):
    print('MIRIM')
    pass
elif (y <= 14):
    print('INFANTIL')
    pass
elif (y <= 19):
    print('JUNIOR')
    pass
elif (y <= 25):
    print('SENIOR')
    pass
else:
    print('MASTER')
    pass
