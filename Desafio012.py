# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com desconto de 5%
preco = int(input('Digite o preço do produto: '))
desconto = preco*(1-(5/100))
print('O valor do produto com desconto de 5% é de {} reais'.format(desconto))