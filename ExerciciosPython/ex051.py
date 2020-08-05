print('-' * 5, '10 Termos de uma Progressão Aritimética', '-' * 5)
ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print('P.A. de {}: '.format(ptermo))
for c in range(ptermo, ptermo+(11-1)*razao, razao):
    print('{}'.format(c), end='-> ')
print('Acabou')
