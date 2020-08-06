# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

r = float(input('Digite um valor em R$: '))
d = r/5.72
print('R${:.2f} é equivalente a ${:.2f}'.format(r, d))
