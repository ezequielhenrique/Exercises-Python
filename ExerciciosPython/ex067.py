# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

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
