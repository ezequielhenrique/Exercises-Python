# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

c = maior = menor = soma = 0
cont = 'S'
while cont in 'Ss':
    n = int(input('Digite um número inteiro: '))
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
print('A média dos valores digitados é {:.1f}'.format(soma / c))
print('O maior valor digitado é {} e o menor é {}'.format(maior, menor))
