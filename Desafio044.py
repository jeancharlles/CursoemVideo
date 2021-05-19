print('{:=^40}'.format(' Loja do Jean '))
preco = float(input('Informe o valor da compra: '))
print('''Escolha a opção de pagamento:
[1] A vista no dinheiro ou cheque com 10% de desconto
[2] A vista no cartão de crédito com 5% de desconto
[3] Parcelado no cartão de crédito em até 2 vezes - preço normal
[4] Parcelado no cartão de crédito em 3 vezes ou mais com juros de 20 %
''')
escolha = int(input('Opção: '))
if escolha == 1:
    print('Você ganhou 10% de desconto {:.2f} reais!'.format(preco-preco*10/100))
elif escolha == 2:
    print('Você ganhou 5% de desconto {:.2f} reais!'.format(preco-preco*5/100))
elif escolha == 3:
    print('Preço normal. Volte sempre! {:.2f} reais'.format(preco))
    print('A sua compra será parcelada em 2x de {:.2f} reais'.format(preco/2))
elif escolha == 4:
    juros = preco+preco*20/100
    print('Sua compra teve um acréscimo de 20% {:.2f} reais '.format(juros))
    parcela = int(input('Informe a quantidade de parcelas: '))
    print('As suas prestações serão de {:.2f} reais'.format(juros/parcela))
else:
    print('\033[0;31m Opção inválida, escolha uma das opções acima.\033[m')
