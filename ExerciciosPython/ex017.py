# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot
catop = float(input('Digite o valor do cateto oposto: '))
catad = float(input('Digite o valor do cateto adjascente: '))
hipot = hypot(catop, catad)
print('O valor da hipotenusa é: {:.2f}'.format(hipot))
