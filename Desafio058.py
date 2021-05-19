from random import randint
comp = randint(1, 10)
print(comp)
n = int(input('Tente advinhar um número de 1 a 10! '))
cont = 0
while n != comp:
    print('Você errou!')
    n = int(input("Digite outro número: "))
    cont += 1
print("Parabéns, você acertou! mas você precisou tentar {} vezes até acertar!".format(cont))

