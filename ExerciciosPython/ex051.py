# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.

print('-' * 5, '10 Termos de uma Progressão Aritimética', '-' * 5)
ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print('P.A. de {}: '.format(ptermo))
for c in range(ptermo, ptermo+(11-1)*razao, razao):
    print('{}'.format(c), end='-> ')
print('Acabou')
