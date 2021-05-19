somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 4):
    print('{:=^20}'.format(p))
    nome = str(input('Digite o nome da {}ª pessoa: '.format(p))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(p)))
    sexo = str(input('Informe o sexo da {}ª pessoa M / F: '.format(p))).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        totmulher20 += 1
media = int(somaidade/3)
print('\nA idade média das pessoas é {}'.format(media))
print('O homem mais velho se chama {} e tem {} anos'.format(nomevelho, maioridadehomem))
print('O total de mulheres com menos de 20 anos é {}.'.format(totmulher20))
