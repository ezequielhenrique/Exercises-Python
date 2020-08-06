# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

jogadores = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    jogos = int(input(f'{jogador["nome"]} jogou quantas partidas? '))
    for c in range(1, jogos+1):
        g = int(input(f'Quantos gols na partida {c}? '))
        gols.append(g)
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    cont = ' '
    while cont != 'S' and cont != 'N':
        cont = str(input('Deseja continuar (S/N): ')).strip().upper()[0]
    if cont == 'N':
        break
print('=*=' * 20)
print('cod ', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:^3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=*=' * 20)
n = 0
while n != 999:
    n = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if n < len(jogadores):
        print(f'  - Levantamento do jogador {jogadores[n]["nome"]}:')
        for i, j in enumerate(jogadores[n]['gols']):
            print(f'     No jogo {i+1} ele fez {j} gols.')
print('-' * 15, 'PROGRAMA ENCERRADO', '-' * 15)
