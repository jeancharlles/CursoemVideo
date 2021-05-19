sexo = str(input("Digite o sexo M para masculino e F para feminino: ")).strip().upper()[0]
while sexo not in "MmFf":
    print('{} não é um sexo válido!'.format(sexo))
    sexo = str(input("Digite o sexo M para masculino e F para feminino: ")).strip().upper()[0]
print("Sexo {} inserido com sucesso! ".format(sexo))
