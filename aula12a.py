nome = (str(input('Digite o seu nome: ')))
arruma = nome.lower()
if arruma == 'jean':
    print('Que nome bonito!')
elif arruma == 'pedro' or arruma == 'maria':
    print('Seu nome é bem popular no Brasil!!')
elif arruma in ('jéssica paolla cláudia isabella'):
    print('Seu nome é bem feminino!')
else:
    print("Seu nome é normal")
print('Tenha um bom dia, {}!'.format(nome.capitalize()))
