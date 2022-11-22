from random import choice

aluno1 = input('Digite o nome de um aluno: ')
aluno2 = input('Digite o nome de um aluno: ')
aluno3 = input('Digite o nome de um aluno: ')
aluno4 = input('Digite o nome de um aluno: ')

alunos = [aluno1,aluno2,aluno3,aluno4]

e = choice(alunos)

print(f'o aluno escolhido foi {e}!')




