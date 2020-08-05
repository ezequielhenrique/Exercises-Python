def moeda(valor=0, moed='R$'):
    txt = f'{moed} {valor:.2f}'
    return txt


def metade(valor, formt=False):
    met = valor / 2
    if formt:
        return moeda(met)
    return met


def dobro(valor, formt=False):
    dob = valor * 2
    if formt:
        return moeda(dob)
    return dob


def aumentar(valor, porc, formt=False):
    aumt = valor * (porc / 100)
    r = valor + aumt
    if formt:
        return moeda(r)
    return r


def diminuir(valor, porc, formt=False):
    dim = valor * (porc / 100)
    r = valor - dim
    if formt:
        return moeda(r)
    return r


def resumo(valor, aumt, dim):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'{"Preço analizado:":<30}{moeda(valor):<10}')
    print(f'{"Dobro do preço:":<30}{dobro(valor, True):<10}')
    print(f'{"Metade do preço:":<30}{metade(valor, True):<10}')
    print(f'{"20% de aumento:":<30}{aumentar(valor, aumt, True):<10}')
    print(f'{"30% de redução:":<30}{diminuir(valor, dim, True):<10}')
    print('-' * 40)
