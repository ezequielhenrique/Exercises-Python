# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual
# foi o maior e o menor peso lidos.

peso = 0
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'A pessoa mais pesada possui {maior}kg.')
print(f'A pessoa mais leve possui {menor}kg.')
