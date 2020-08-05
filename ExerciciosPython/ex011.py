l = float(input('Qual a largura da parede (m): '))
h = float(input('Qual a altura da parede (m): '))
area = l*h
t = area/2
print('A quantidade de tinta necessária para pintar uma parede de {:.2f}m² é {:.2f}litros'.format(area, t))
