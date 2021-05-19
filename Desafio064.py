cont = n = soma = 0
while n !=999:
    n = int(input("Digite um número ou 999 para parar: "))
    cont += 1
    if n != 999:
        soma += n
print("Foram digitados {} números e a soma destes números é {}. ".format(cont, soma))
print("FIM")
