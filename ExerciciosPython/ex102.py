# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.


def fatorial(n, show=False):
    """
    -> Função que calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) mostra ou não o cálculo
    :return: O valor do fatorial do número n
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
    return f


# Programa principal
print(fatorial(5))
print(fatorial(5, show=True))
print(fatorial(10, show=False))

help(fatorial)
