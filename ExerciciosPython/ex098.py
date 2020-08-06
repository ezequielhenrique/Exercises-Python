# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:

from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    c = inicio

    if inicio < fim:
        while c <= fim:
            print(c, end=' ')
            c += passo
            sleep(1)
    if inicio > fim:
        while c >= fim:
            print(c, end=' ')
            c -= passo
            sleep(1)
    print('Fim')


def linha():
    print('=*=' * 20)


# Programa Principal
linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora é sua vez! Personalize a contagem.')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
linha()
contador(i, f, p)
linha()
