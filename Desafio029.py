v = float(input('Informe a sua velocidade: '))
if v > 80:
    print('Você ultrapassou o limite de velocidade!')
    print('A multa aplicada é de R$ {:.2f} reais'. format((v-80)*7))
print('Parabéns você é um ótimo motorista!')
