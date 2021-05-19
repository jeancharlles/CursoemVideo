frase = str(input('Digite a frase: ')).strip().upper()#strip tira as pontas da frase
palavra = frase.split()#tira os meios da frase
junto = ''.join(palavra) #junta todas as palavras

#                 JEITO Simples do Python sem o for, com fatiamento
inverso = junto[::-1]
print(inverso, '', junto)
if inverso == junto:
    print('\nEstas palavras são um PALÍNDROMO!')
else:
    print('\nEstas palavras não são um palíndromo.')
