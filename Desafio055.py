for p in range(1, 4):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
print('O maior peso informado foi {} kg'.format(maior))
print('O menor peso informado foi {} kg'.format(menor))
