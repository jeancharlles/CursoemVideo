imovel = float(input('Informe o valor do imóvel que deseja comprar: '))
tempo = int(input('Informe em quantos anos deseja pagar este imóvel: '))
salario = float(input('Informe o valor do seu salário: '))
prestação = (imovel/tempo)/12
print('A prestação do imóvel fica em: {:.2f}'.format(prestação))
capacidade = salario*0.3
print('A sua capacidade de compra é de até: {:.2f}'.format(capacidade))
if prestação > capacidade:
    print('Você não é capaz de comprar este imóvel')
elif prestação < capacidade:
    print('Você é capaz de comprar este imóvel')
