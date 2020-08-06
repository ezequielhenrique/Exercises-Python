# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

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
