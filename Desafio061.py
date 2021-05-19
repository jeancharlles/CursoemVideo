primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
pa = (razao + primeiro)
cont = 1
while cont < 10:
    if cont == 1:
        print(primeiro, end=" -> ")
    cont += 1
    print(pa, end=" -> ")
    pa += razao
print("FIM!")


