# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem.

n1 = int(input('Didite um número inteiro: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O primeiro número é maior, {} > {}.'.format(n1, n2))
elif n1 < n2:
    print('O segundo número é maior, {} > {}.'.format(n2, n1))
else:
    print('Os números são iguais.')
