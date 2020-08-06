# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
print('-' * 50)
print('JOGO DA MEGA SENA'.center(50))
print('-' * 50)
jogos = list()
n = int(input('Quantos jogos você deseja sortear? '))
print('-' * 10, f'Sorteando {n} jogos', '-' * 10)
tot = 0
while tot < n:
    cont = 0
    tot += 1
    while True:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    print(f'Jogo {tot}: {jogos}')
    jogos.clear()
    sleep(1)
print('-' * 10, 'Boa Sorte!', '-' * 10)
