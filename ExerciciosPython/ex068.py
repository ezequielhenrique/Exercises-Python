from time import sleep
from random import randint
c = 0
print('-=' * 10, 'JOGO DO PAR OU ÍMPAR', '-=' * 10)
while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(1, 10)
    soma = jogador + pc
    op = ' '
    while op not in 'PpIi':
        op = str(input('Você escolhe par ou ímpar (P/I)? ')).strip().upper()[0]
    sleep(1)
    print('-' * 60)
    print(f'Você jogou {jogador} e o computador {pc}, ', end='')
    if soma % 2 == 0:
        print(f'Total de {soma}, resultado PAR.')
        result = 'P'
    else:
        print(f'Total de {soma}, resultado ÍMPAR.')
        result = 'I'
    print('-' * 60)
    sleep(1)
    if result == op:
        print('Parabéns, você venceu!!')
    else:
        print('Você perdeu!')
        break
    c += 1
print(f'Você venceu {c} vezes')
