print("_"*30)
print("\nSequência de Fibonnacci")
print("_"*30)
termos = int(input("Quantos termos você quer mostrar? "))
cont = 1
v = 1
apoio = 0
r = 0
while cont <= termos:
    r = v + apoio
    print("{}".format(r), end=" ")
    apoio = v
    v = r
    cont += 1
print("\nFIM")
