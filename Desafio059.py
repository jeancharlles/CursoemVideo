escolha = 0
while escolha != 5:
    n1 = int(input('\nDigite um número: '))
    n2 = int(input('Digite um número: '))
    print('\n[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Novos números')
    print('[5] - Sair do programa')
    escolha = int(input('\nEscolha a opção acima: '))
    if escolha == 1:
        print(n1+n2)
    elif escolha == 2:
        print(n1*n2)
    elif escolha == 3:
        if n1 > n2:
            print('{} é o maior número'.format(n1))
        else:
            print('{} é o maior número!'.format(n2))
print('FIM')
