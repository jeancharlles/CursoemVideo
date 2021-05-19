n = int(input('Digite um número: '))
p = n
fatorial = 1
while not n == 1:
    fatorial *= n
    n = n-1
print('Fatorial de {} é {}'.format(p, fatorial))
