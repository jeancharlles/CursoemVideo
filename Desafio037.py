n = int(input('Digite um número: '))
print(''' Escolha as opções abaixo:
1 - para converter em binário
2 - para converter em octal
3 - para converter em hexadecimal''')
opcao = int (input('Escolha uma das opções acima: '))
if opcao == 1:
    print('O número {} convertido em binário é {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('O número {} convertido em octal é {}'.format(n, oct(n)[2:]))
elif opcao ==3:
    print('O número {} convertido em hexadecimal é {}'.format(n, hex(n)[2:].upper()))
else:
    print('Opção inválida tente novamente!')

