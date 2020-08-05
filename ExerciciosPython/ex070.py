print('-' * 40)
print('MERCADO VIRTUAL'.center(40))
print('-' * 40)
tot = tot1000 = preco_barato = c = 0
nome_barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    tot += preco
    if preco >= 1000:
        tot1000 += 1
    if c == 0 or preco < preco_barato:
        nome_barato = produto
        preco_barato = preco
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
    if op == 'N':
        break
    c += 1
print('-' * 40)
print(f'''O total da compra foi R$ {tot:.2f}
Há {tot1000} produtos que custam mais de R$ 1000.00
O produto mais barato foi o(a) {nome_barato} que custa R$ {preco_barato:.2f}''')
