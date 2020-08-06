# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
# tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Qual a largura da parede (m): '))
h = float(input('Qual a altura da parede (m): '))
area = l*h
t = area/2
print('A quantidade de tinta necessária para pintar uma parede de {:.2f}m² é {:.2f}litros'.format(area, t))
