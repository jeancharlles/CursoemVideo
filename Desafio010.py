# Crie um programa que leia quanto dinheiro a pessoa tem, e mostre quantos dolares ela pode comprar. O dolar vale 3,27
dinheiro = float(input("Digite quanto você tem na carteira: "))
dolar = (dinheiro/3.27)
print('Com {} reais você consegue comprar {:.2f} dolares'.format(dinheiro, dolar))