#Faça um programa que leia o cumprimento do triangulao do cateto oposto e o cateto adjacente
#Calcule e mostre o comprimento da hipotenusa

import math
co = float(input('Digite o valor do cateto oposto do triângulo: '))
ca = float(input('Digite o valor do cateto adjacente do triângulo: '))
h= math.sqrt(math.pow(ca,2)+math.pow(co,2))
print('O valor da hipotenusa é: {:.2f}'.format(h))