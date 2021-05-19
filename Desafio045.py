from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha uma das opções abaixo:
[0] Pedra
[1] Papel 
[2] Tesoura
''')
parabens = str('Parabéns você ganhou o jogo!!\n')
perda = str('Que pena você perdeu')
jogador = int(input('Faça a sua jogada: '))
if jogador != 2 and jogador != 1 and jogador !=0:
    print('Jogada invalida! Jogue novamente!')
else:
    print('O jogador escolheu {}'.format(itens[jogador]))
    print('O computador escolheu {}'.format(itens[computador]))
    sleep(2)
    print('\nJO')
    sleep(2)
    print('KEN')
    sleep(2)
    print('PÔ\n')
    sleep(2)
    if jogador == computador:
        print('\nJogo empatado')
        print('O jogador escolheu {} e o computador escolheu {}'.format(itens[jogador], itens[computador]))
    else:
        if jogador == 0:
            if computador == 2:
                print(parabens,'Você escolheu {} e o computador escolheu {}!'.format(itens[jogador], itens[computador]))
                print('{} ganha de {}'.format(itens[jogador], itens[computador]))
            else:
                print(perda)
        elif jogador == 1:
            if computador == 0:
                print(parabens,'Você escolheu {} e o computador escolheu {}!'.format(itens[jogador], itens[computador]))
                print('{} ganha de {}'.format(itens[jogador], itens[computador]))
            else:
                print(perda)
        elif jogador == 2:
            if computador == 1:
                print(parabens, 'Você escolheu {} e o computador escolheu {}!'.format(itens[jogador], itens[computador]))
                print('{} ganha de {}'.format(itens[jogador], itens[computador]))
            else:
                print(perda)
        else:
            print('Jogada inválida!')
