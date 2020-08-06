# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
num = float(input('Digite um número real: '))
convert = math.floor(num)
print('Sua representação nos inteiros é: {}'.format(convert))
