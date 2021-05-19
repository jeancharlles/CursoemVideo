print('Digite a seguir os 3 lados do triângulo:')
lado1 = int(input('Lado1 = '))
lado2 = int(input('Lado2 = '))
lado3 = int(input('Lado3 = '))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado3 + lado2 > lado1:
    print('Este é um triângulo ', end='')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO')
    elif lado1 != lado2 != lado3 != lado1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Este não é um triângulo')
