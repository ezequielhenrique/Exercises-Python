# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número inteiro: '))
ant = n-1
suc = n+1
print('O antecessor de {} é {} e o sucessor é {}'.format(n, ant, suc))
