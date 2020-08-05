def linha(tam=40):
    print('~' * tam)


def cabecalho(txt):
    linha()
    print(f'{txt}'.center(40))
    linha()


def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[031m[ERRO] por favor, digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('Programa interrompido pelo usuário')
        else:
            return n


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[34m{c} - {i}\033[m')
        c += 1
    linha()
    opc = leiaInt('\033[36mSua opção: \033[m')
    return opc
