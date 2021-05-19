peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso/altura**2
print('IMC = {:.2f} '.format(imc), end='')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Peso Ideal')
elif 25 < imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
