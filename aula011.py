print('\033[4;30;45m Olá mundo! sublinhado\033[m')
print('\033[0;30;41m Letra branca e fundo vermelho sem limite')
print('\033[1;31;43m Letra vermelha em negrito e fundo amarelo com limite \033[m')
print('\033[7;30m Letra branca e fundo preto e depois inverte para fundo branco e letra preta\033[m')
a = 3
b = 5
print('Os valores são \033[34m{}\033[m e \033[31m{}\033[m'.format(a, b))
nome = 'Jean'
print('Olá prazer em te conhecer {}{}{}!!'.format('\033[34m', nome, '\033[m'))
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'azul': '\033[34m'
         }
print('Olá {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))
