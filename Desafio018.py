#Faça um programa que leia um angulo qualquer e que mostre na tela o valor do seno,co-seno e tangente

import math
angulo = float(input('Digite o valor de um ângulo: '))
seno = (math.sin(math.radians(angulo)))
cosseno = (math.cos(math.radians(angulo)))
tangente = (math.tan(math.radians(angulo)))
print('O ângulo {} possui\n o seno de {:.2f},\n o cosseno de {:.2f}\n e a tangente de {:.2f}.'.format(angulo, seno, cosseno, tangente))

