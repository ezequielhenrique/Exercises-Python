print('-' * 5, '10 Termos de uma Progressão Aritimética (v2.0)', '-' * 5)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
print('P.A = ', end='')
while c <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    c += 1
print('Acabou')
