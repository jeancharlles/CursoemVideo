primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
pa = (razao + primeiro)
cont = 1
termos = 0
while cont < 10:
    if cont == 1:
        print(primeiro, end=" -> ")
    cont += 1
    print(pa, end=" -> ")
    pa += razao
    termos +=1
opção = int(input("\nQuantas termos mais você quer desta PA? "))
while opção != 0:
    contador = 0
    while contador < opção:
        print(pa, end=" ->")
        pa += razao
        contador += 1
        termos +=1
    opção = int(input("\nQuantas termos mais você quer desta PA? "))
print("\nForam calculados {} termos desta PA.".format(termos+1))
print("FIM!")
