def fatorial(num=1):
    """
    -> Função que calcula o fatorial de um número
    :param num: Número que será calculado o fatorial
    :return: Fatorial do número
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(3)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')
