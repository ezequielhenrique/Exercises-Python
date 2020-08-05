km = float(input('Quantidade de km percorridos pelo carro: '))
dias = int(input('Quantidade de dias que foi alugado: '))
custo = (dias*60) + (km*0.15)
print('O valor do aluguel do carro é: R${:.2f}'.format(custo))
