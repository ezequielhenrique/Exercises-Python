# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime
ano = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    if datetime.today().year - ano < 18:
        menor += 1
print('Das 7 pessoas {} são menores de idade e {} são maiores de idade.'.format(menor, 7-menor))
