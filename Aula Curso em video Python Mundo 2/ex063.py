n = int(input('NÙMERO: '))
b = 1
n1 = 0
n2 = 1

print(f'a posição {1} da sequencia de fibonacci é {0}')

while b < n:
    seq_poss = n1 + n2
    print(f'a posição {b+1} da sequencia de fibonacci é {seq_poss}')
    n2 = n1
    n1 = seq_poss
    b += 1
