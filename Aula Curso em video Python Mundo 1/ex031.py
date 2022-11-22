d = int(input('digite a distancia percorrida '))


if(d > 200):
    preco = d * 0.45
else:
    preco = d * 0.50

print(f'por {d} Km você paragá {preco} R$! ')


