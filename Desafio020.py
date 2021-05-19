# Faça um algoritmo que leia o nome de quatro alunos e determina a ordem de apresentação de trabalho destes alunos

from random import shuffle
a1 = str(input('Digite o nome do aluno: '))
a2 = str(input('Digite o nome do aluno: '))
a3 = str(input('Digite o nome do aluno: '))
a4 = str(input('Digite o nome do aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem escolhida dos alunos foi: \n',lista)