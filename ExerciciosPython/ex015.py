# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantidade de km percorridos pelo carro: '))
dias = int(input('Quantidade de dias que foi alugado: '))
custo = (dias*60) + (km*0.15)
print('O valor do aluguel do carro é: R${:.2f}'.format(custo))
