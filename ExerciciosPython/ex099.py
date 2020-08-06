# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*num):
    m = 0
    print('~' * 50)
    print('Analisando os valores passados...')
    sleep(2)
    for n in num:
        print(n, end=' ')
        if n > m:
            m = n
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {m}')
    sleep(1)


maior(4, 8, 9, 7, 2, 3)
maior(10, 15, 7)
maior(3)
maior()
