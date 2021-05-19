# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e sua raiz quadrada

n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print(' O número {} tem como dobro {}, \n o triplo {}, \n e a raiz quadrada {:.2f} '.format(n, d, t, r))