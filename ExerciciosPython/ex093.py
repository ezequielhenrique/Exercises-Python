# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo
# isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

from time import sleep
jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome: ')).strip()
p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1, p+1):
    g = int(input(f'Quantos gols na partida {c}? '))
    gols.append(g)
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('=*=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} possui o valor {v}.')
print('=*=' * 20)
print(f'{jogador["nome"]} jogou {len(gols)} partidas:')
for p, i in enumerate(gols):
    sleep(1)
    print(f'  -Na partida {p+1}, fez {i} gols.')
print(f'Um total de {jogador["total"]} gols.')
