# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Digite o valor do ângulo: '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O cosseno de {}º é: {:.2f}'.format(ang, cos))
print('O seno de {}º é: {:.2f}'.format(ang, sen))
print('A tangente de {}º é: {:.2f}'.format(ang, tg))
