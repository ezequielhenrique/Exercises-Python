dist = float(input('Qual a distância da sua viagem em Km: '))
valor = 0
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45
print('O valor da sua viagem será: R${:.2f}'.format(valor))
