# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci.

print('-' * 5, 'SEQUÊNCIA DE FIBINACCI', '-' * 5)
n = int(input('Digite o número de termos: '))
c = 3
ptermo = 0
stermo = 1
print('{}, {}, '.format(ptermo, stermo), end='')
while c <= n:
    ttermo = ptermo + stermo
    print('{}, '.format(ttermo), end='')
    ptermo = stermo
    stermo = ttermo
    c += 1
print('Fim')
