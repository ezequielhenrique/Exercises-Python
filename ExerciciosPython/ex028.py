# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu
# ou perdeu.

import random
from time import sleep

pc = random.randint(0, 5)       # Gera um número entre 0 e 5
print('\033[1;34m-=' * 30)
print('Vou pensar em um número entre 0 e 5, tente advinhar!')
print('-=' * 30)
num = int(input('\033[mEm que número eu pensei? '))         # Ojogador tenta advinhar
print('\033[36mPROCESSANDO...\033[m')
sleep(2)
if num == pc:
    print('Parabéns, você venceu')
else:
    print('Você perdeu, o número correto era o {}'.format(pc))
    print('Tente Novamente')
