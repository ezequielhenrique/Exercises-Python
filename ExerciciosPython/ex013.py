# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Qual o valor do salário? '))
aum = s+(s*(15/100))
print('O salário atual é R${:.2f}'.format(s))
print('O novo valor do salário com aumento de 15% é R${:.2f}'.format(aum))
