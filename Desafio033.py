n1 = int(input('\nDigite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

#Jeito simples
print('\nJeito simples:')
print('O menor número é: {}'.format(min(n1, n2, n3)))
print('O maior número é: {}\n'.format(max(n1, n2, n3)))

#Jeito Guanabara
#Verificando o menor
print('\nJeito Guanabara:')
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor número é: {}'.format(menor))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print("O maior número é: {}".format(maior))

#Jeito complicado
#Verificando o menor
print('\nJeito Complicado')
if (n1 < n2) and (n1 < n3):
    print('O menor número é: {}'.format(n1))
if (n2 < n1) and (n2 < n3):
    print('O menor número é: {}'.format(n2))
if (n3 < n2) and (n3 < n1):
    print('O menor número é: {}'.format(n3))

if (n1 > n2) and (n1 > n3):
    print('O maior número é: {}'.format(n1))
if (n2 > n1) and (n2 > n3):
    print('O maior número é: {}'.format(n2))
if (n3 > n1) and (n3 > n2):
    print('O maior número é: {}'.format(n3))