for c in range(1, 10, 3):
    print(c)
print('FIM\n')

for c in range(6, 1, -1):
    print(c)
print('FIM\n')

inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim'))
passo = int(input('Digite o passo'))
for c in range(inicio, fim+1, passo):
    print(c)
print('FINAL\n')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
    print(n)
print('A soma de todos os valores é igual a {}'.format(s))


