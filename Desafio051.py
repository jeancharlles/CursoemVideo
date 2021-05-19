a1 = int(input('Digite o primeiro número da PA: '))
r = int(input('Digite a razão: '))
an = r*10+a1
for c in range(a1, an, r):
    print('{}'.format(c), end=' -> ')
print('ACABOU!')
