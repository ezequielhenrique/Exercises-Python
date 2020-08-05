from random import randint
from time import sleep

print('\033[1;32m-=' * 9, 'JOGO DA ADIVINHAÇÃO', '-=' * 9)
print('-' * 55)
print('\033[mVou pensar em um número entre 0 e 10, tente advinhar: ')
pc = randint(0, 10)
acertou = False
c = 0
while not acertou:
    usuario = int(input('Em qual número eu pensei? '))
    c += 1
    sleep(1)
    if usuario != pc:
        if usuario < pc:
            print('Mais! Tente outra vez.')
        else:
            print('Menos! Tente outra vez.')
    else:
        acertou = True
print('Você venceu!!!\nForam necessárias {} tentativas.'.format(c))
