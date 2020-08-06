# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('-' * 40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-' * 40)
produtos = ('Lápis', 1.50, 'Borracha', 2.00, 'Caderno', 35.50, 'Livro', 54.99, 'Compasso', 7.00,
            'Régua', 4.50, 'Escalímetro', 20.70, 'Transferidor', 5.90, 'Mochila', 125.50)
for c in produtos:
    if type(c) is str:
        print(f'{c:.<31}R$', end='')
    if type(c) is float:
        print(f'{c:>7.2f}')
print('-' * 40)
