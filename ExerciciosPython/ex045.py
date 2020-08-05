from random import choice
from time import sleep

print('-=' * 10, 'Jokenpô', '-=' * 10)
jogador = str(input('Escolha pedra, papel ou tesoura: ')).title().strip()
pc = choice(['Pedra', 'Papel', 'Tesoura'])      # O computador escolhe uma das opções

if jogador == 'Pedra' or jogador == 'Papel' or jogador == 'Tesoura':
    print('--' * 24)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print('--' * 24)
    if jogador == pc:
        print('O computador escolheu {}, empate!\nTente novamente'.format(pc))
    elif jogador == 'Tesoura' and pc == 'Papel':
        print('O computador escolheu {}\nParabéns, você venceu!'.format(pc))
    elif jogador == 'Papel' and pc == 'Pedra':
        print('O computador escolheu {}\nParabéns, você venceu!'.format(pc))
    elif jogador == 'Pedra' and pc == 'Tesoura':
        print('O computador escolheu {}\nParabéns, você venceu!'.format(pc))
    else:
        print('O computador escolheu {},\nO computador venceu.'.format(pc))
else:
    print('Opção inválida, tente novamente.')
