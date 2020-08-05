# Gera números aléatórios em uma tupla e indica os menores e os maiores valores

from random import randint
sort = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for c in sort:
    print(f'{c} ', end='')
print(f'\nO maior número sorteado foi: {max(sort)}')
print(f'O menor número sorteado foi: {min(sort)}')
