def leia_dinheiro(txt):
    while True:
        valor = input(txt).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[31m[ERRO] \'{valor}\' é um preço inválido\033[m')
        else:
            valor = float(valor)
            break
    return valor
