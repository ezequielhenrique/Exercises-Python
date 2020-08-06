# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o
# empréstimo será negado.

print('-'*10, 'APROVAÇÃO DE FINANCIAMENTO', '-'*10)
casa = float(input('Qual o valor da casa que você quer financiar? R$'))
salario = float(input('Qual o valor de seu salário? R$'))
anos = int(input('Em quantos anos você deseja financiar a casa? '))
prestacao = casa / (anos*12)
if prestacao <= salario*(30/100):
    print('Parabéns! Seu financiamento foi aprovado.')
    print('O valor da prestação mensal será R${:.2f} durante {} meses.'.format(prestacao, anos*12))
else:
    print('Para financiar essa casa em {} anos custará R${:.2f} por mês.'.format(anos, prestacao))
    print('Infelizmente você não pode financiar essa casa.')
