primo = int(input('Digite um número para saber se ele é primo: '))
cont = 0
for c in range(1, primo+1):
        if primo % c == 0:
            print('\033[0;31;m{}'.format(c), end=' ')
            cont += 1
        else:
            print('\033[0;33;m{}'.format(c), end=' ')
if cont == 2:
    print('\n\033[mO número {} foi divisível apenas {} vezes, portanto ele é primo!!!'.format(primo, cont))
else:
    print('\n\033[mO número {} foi divisível por {} números, portanto ele não é primo!'.format(primo, cont))

