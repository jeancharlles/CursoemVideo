import random
from time import sleep
n = int(random.randint(0, 5))
num = int(input('Advinhe um número de 0 a 5 : '))
print('Processando...')
sleep(3)
print('Parabéns você acertou!' if n == num else 'Que pena, você errou!')
