# Maior e menor valores de uma lista

num = []
maior = menor = 0
for c in range(0, 5):
    num.append(int(input('Digite um número inteiro: ')))
    if c == 0:
        maior = num[c]
        menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print(f'Os valores digitados foram {num}')
print(f'O maior número da lista é o {maior} que está nas posições ', end='')
for p, n in enumerate(num):
    if n == maior:
        print(f'{p}...', end='')
print(f'\nO menor número da lista é o {menor} que está nas posições ', end='')
for p, n in enumerate(num):
    if n == menor:
        print(f'{p}...', end='')
