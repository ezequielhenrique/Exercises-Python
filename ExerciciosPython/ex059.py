# Programa que lê dois valores e mostra um menu na tela:

from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
sair = False
while not sair:
    print('Qual operação você deseja realizar?')
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa''')
    op = int(input('>>>>>> Qual é a sua opção: '))
    sleep(1)
    print('-' * 40)
    if op == 1:
        print('A soma entre {} e {} é {}.'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('O valor do produto entre {} e {} é {}.'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 == n2:
            print('Os números são iguais.')
        elif n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
        else:
            print('{} é maior que {}.'.format(n2, n1))
    elif op == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        sair = True
    else:
        print('Valor inválido, tente novamente!')
    print('-' * 40)
sleep(1)
print('-' * 10, 'PROGRAMA ENCERRADO', '-' * 10)
