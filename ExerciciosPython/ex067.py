print('\033[1;30m-=' * 5, 'TABUADA v3.0', '-=' * 5)
while True:
    n = int(input('\033[mTabuada do número: '))
    print('-' * 34)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c}')
    print('-' * 34)
print('---Programa encerrado---')
