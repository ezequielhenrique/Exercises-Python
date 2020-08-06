# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
# em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou
# o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
dados = dict()
ranking = list()
for c in range(1, 5):
    dados[f'Jogador {c} '] = randint(1, 6)
print('Valores sorteados:')
sleep(1)
for k, v in dados.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
print('-' * 30)
print('Ranking dos jogadores:')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
c = 1
for k, v in ranking:
    print(f'{c}º lugar: {k} tirou {v} no dado')
    c += 1
    sleep(1)
