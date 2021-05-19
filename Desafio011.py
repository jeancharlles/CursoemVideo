# Faça um programa que leia a largura e a altura de uma parede e calcule a sua área.
# Calcule a quantidade necessária para pintar uma parede considerando que cada litro de tinta pinta 2m²
altura = int(input('Digite a altura da parede: '))
largura = int(input('Digite a largura da parede: '))
area = altura*largura
tinta = area/2
print('A parede tem {}m² \n e será necessário {} litros de tinta para pintar a parede'.format(area,tinta))