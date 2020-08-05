preco = float(input('Qual o valor do produto: R$'))
print('''Condição de pagamento:
[1] À vista, dinheiro/cheque (10% de desconto)
[2] À vista no cartão (5% de desconto)
[3] Em até 2x no cartão (preço normal)
[4] Em 3x ou mais no cartão (20% de juros)''')
op = int(input('Opção: '))
desc = preco
if op < 5:
    if op == 1:
        desc = preco - (preco*(10/100))
    elif op == 2:
        desc = preco - (preco*(5/100))
    elif op == 3:
        desc = preco
    elif op == 4:
        desc = preco + (preco*(20/100))
    print('O valor a ser pago será: R${:.2f}'.format(desc))
else:
    print('Opção inválida, tente novamente')
