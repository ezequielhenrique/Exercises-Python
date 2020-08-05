# Sistema utilizando o interactive help do Python

cores = {
    '': '\033[m',
    'Azul1': '\033[1;30;44m',
    'Azul2': '\033[30;46m',
    'Branco': '\033[7;30;47m',
    'Vermelho': '\033[1;30;41m'
}


def escreva(txt, cor=''):
    t = len(txt) + 6
    print(cores[cor], end='')
    print('~' * t)
    print(f'{txt:^{t}}')
    print('~' * t)
    print(cores[''], end='')


def ajuda():
    from time import sleep
    while True:
        escreva('SISTEMA DE AJUDA PyHELP', 'Azul1')
        f = str(input('Função ou biblioteca > ')).strip()
        if f == 'fim':
            sleep(2)
            break
        escreva(f'Acessando o manual do comando \'{f}\'', 'Azul2')
        sleep(2)
        print(cores['Branco'], end='')
        help(f)
        print(cores[''], end='')
    escreva('Até Logo!', 'Vermelho')


ajuda()
