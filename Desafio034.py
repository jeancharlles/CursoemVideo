salario = float(input('Informe qual é o seu salário atual: '))
if salario > 1250:
    print('O seu aumento foi de 10% R$ {:.2f}'.format(salario*1.10))
else:
    print('O seu aumento foi de 15% R$ {:.2f}'.format(salario*1.15))
