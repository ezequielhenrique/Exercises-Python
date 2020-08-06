# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('-' * 10, 'Tabuada', '-' * 10)
n = int(input('Tabuada do número: '))
for c in range(1, 10+1):
    print('{} x {:2} = {}'.format(n, c, n*c))
