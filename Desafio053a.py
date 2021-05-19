frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
print('A variável palavras usando split: ', palavras)
junto = ''.join(palavras)
print('A variável junto usando join: ', junto)
inverso = ''
print('Você digitou a frase {}'.format(frase))
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
    print(junto[letra]) 
print(junto, inverso)
if junto == inverso:
    print('Esta frase é um palíndromo')
    print('{} é palíndromo de {}'.format(junto,inverso))
else:
    print('Esta frase não é um palíndromo')
