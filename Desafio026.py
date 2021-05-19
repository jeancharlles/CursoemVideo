frase = str(input('Digite algo: ')).strip().lower()
print('Na frase temos {} letras A'.format(frase.count('a')))
print('O primeiro A começa na posição {}'.format(frase.find('a')+1))
print('A última letra A termina na posição {}'.format(frase.rfind('a')+1))