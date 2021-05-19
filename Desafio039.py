from datetime import date
ano = int(input('Digite o ano de nascimento: '))
atual = date.today().year
if atual - ano > 18:
    print('O seu alistamento já passou há {} anos'.format(atual-ano-18))
    print('Você deveria se alistar em {}'.format(atual-(atual-ano-18)))
elif atual - ano < 18:
    print('O seu alistamento será daqui a {} ano(s)'.format(18-(atual-ano)))
    print('O seu alistamento será em {}'.format(atual+(18-(atual-ano))))
else:
    print('O seu alistamento será neste ano')
    print('O seu alistamento será em {}'.format(atual))
