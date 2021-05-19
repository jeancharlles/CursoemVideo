#jEITO Guanabara
cont = n = soma = 0
n = int(input("Digite um número ou 999 para parar: "))
while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite um número ou 999 para parar: "))
print("Foram digitados {} números e a soma destes números é {}. ".format(cont, soma))
print("FIM")
