# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.

from random import randint


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        print(n, end=' ')
        lista.append(n)
    print('Fim')


def soma_par(lista):
    print(f'Somando os valores pares de {lista}, ', end='')
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'soma igual a {soma}')


num = list()
sorteia(num)
soma_par(num)
