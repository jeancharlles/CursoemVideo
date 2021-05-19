s = 0
cont = 0
for c in range(1, 10, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print('A soma de todos os {} números ímpares múltiplos de 3 é: {}'.format(cont, s))

cont = 0
s = 0

# Ou podemos fazer assim

for c in range(0, 10):
    if c % 3 == 0 and c % 2 != 0:
        cont += 1
        s += c
print('A soma de todos os {} números ímpares múltiplos de 3 é: {}'.format(cont, s))
