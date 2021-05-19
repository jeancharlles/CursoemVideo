d = float(input('Digite a distância em quilometros da sua viagem: '))
if d > 200:
    print('A sua passagem irá custar {:.2f} reais'.format(d*0.45))
else:
    print('A sua passagem irá custar {:.2f} reais'.format(d*0.5))
