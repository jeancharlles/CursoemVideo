#import math #importa toda a biblioteca math
from math import sqrt,ceil #importa apenas a função sqrt da biblioteca math
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, raiz))
#print('A raiz quadrada de {} é igual ao arredondamento para baixo {:.2f}'.format(num, math.floor(raiz)))
print('A raiz quadrada de {} é igual ao arredondamento para cima {:.2f}'.format(num, ceil(raiz)))