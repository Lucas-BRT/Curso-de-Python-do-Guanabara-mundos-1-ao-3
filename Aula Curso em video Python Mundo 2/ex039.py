import datetime

ano = str(datetime.date.today())
ano = int(ano[0:4])

nascimento = int(input('DIGITE O ANO DO SEU NASCIMENTO: '))

ser = ano - nascimento

print(ser)

if(ser < 18):
    print(f'VOCÊ IRÁ SERVIR EM {ser - 18} ANOS')
elif(ser == 18):
    print(f'VOCÊ IRÁ SERVIR ESSE ANO!')
else:
    print(f'VOCÊ DEVERIA TER SERVIDO A {ser - 18} ANOS ATRÁS')










