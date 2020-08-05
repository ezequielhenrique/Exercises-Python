palavras = ('Aprender', 'Programar', 'Python', 'Xadrez', 'Matemática', 'Cálculo',
            'Física', 'Poker', 'Futebol', 'Automação')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aáãeiíou':
            print(letra, end=' ')
