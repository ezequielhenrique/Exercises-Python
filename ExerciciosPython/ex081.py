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
