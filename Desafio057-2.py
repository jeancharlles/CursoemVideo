sexo = str(input('Digite o sexo M para masculino e F para Feminino: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos! Digite novamente: ')).strip().upper()[0]
print('Sexo {} inserido com sucesso!'.format(sexo))
