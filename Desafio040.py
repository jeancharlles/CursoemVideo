nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2)/2
if media >= 7:
    print('Aluno aprovado! Sua média foi {}'.format(media))
#elif media >5 and media <7:
elif 7 > media >= 5:
    print('Aluno em recuperação! Sua média foi {}'.format(media))
else:
    print('Aluno reprovado! Sua média foi {}'.format(media))