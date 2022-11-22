f = input('Digite uma frase: ')

fa = f.lower().count('a')

print(f'a letra "a" aparece no texto digitado {fa} vezes ')

fa = f.lower().find('a')

print(f'a letra "a" aparece pela primeira vez no digito {fa+1}  ')

fa = f.lower().rfind('a')

print(f'a letra "a" aparece pela ultima vez no digito {fa+1}  ')

