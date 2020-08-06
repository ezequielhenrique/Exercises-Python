# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.


def area(l1, l2):
    a = l1 * l2
    print(f'A área de um terreno de {l1}x{l2} é de {a:.2f}m²')


print('-' * 10, 'ÁREA DO TERRENO', '-' * 10)
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)
