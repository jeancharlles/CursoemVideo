# Jeito Guanabara----
print('Gerador de PA')
print("=="*10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
            print("{}".format(termo), end=" -> ")
            termo += razao
            cont += 1
    print("\nPausa")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Total de termos {}".format(total))
print("FIM!")
