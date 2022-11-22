import random

aluno1 = str(input('Digite o nome de um aluno: '))
aluno2 = str(input('Digite o nome de um aluno: '))
aluno3 = str(input('Digite o nome de um aluno: '))
aluno4 = str(input('Digite o nome de um aluno: '))

alunos = [aluno1,aluno2,aluno3,aluno4]

e = random.sample(alunos, 4 )
print(e)
print(f'o aluno escolhido foi {e}!')





















