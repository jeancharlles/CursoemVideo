# Faça um algoritmo que leia o salário de um funcionário e calcule 15% de aumento.
salario = int(input('Informe o salário do funcionário '))
aumento = salario*(1+(15/100))
print('O valor do aumento de 15% do salário é de {:.2f} reais'.format(aumento))