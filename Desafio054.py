from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
ano = 0
idades = str()
for p in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(p)))
    if atual - ano > 21:
        totmaior += 1
    else:
        totmenor += 1
    idades += str(ano)
print('Foram digitadas as idades de {} maiores de idade e {} menores de idade.'.format(totmaior, totmenor))
