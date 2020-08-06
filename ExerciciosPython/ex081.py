# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

num = []
while True:
    num.append(int(input('Digite um número inteiro: ')))
    op = ' '
    while op != 'S' and op != 'N':
        op = str(input('Deseja continuar (S/N): ')).strip().upper()[0]
    if op == 'N':
        break
print('-' * 30)
print(f'Foram digitados {len(num)} números.')
num.sort(reverse=True)
print(f'Lista em ordem decrescente: {num}')
if 5 in num:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')
