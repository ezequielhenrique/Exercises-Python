print('-' * 10, 'Tabuada', '-' * 10)
n = int(input('Tabuada do número: '))
for c in range(1, 10+1):
    print('{} x {:2} = {}'.format(n, c, n*c))
