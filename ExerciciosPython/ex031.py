# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
# R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Qual a distância da sua viagem em Km: '))
valor = 0
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45
print('O valor da sua viagem será: R${:.2f}'.format(valor))
