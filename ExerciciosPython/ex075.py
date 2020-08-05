numbers = (int(input('Digite um número inteiro: ')),
           int(input('Digite um número inteiro: ')),
           int(input('Digite um número inteiro: ')),
           int(input('Digite um número inteiro: ')))
print(f'Você digitou os valores {numbers}')
print(f'O número nove apareceu {numbers.count(9)} vezes.')
if 3 in numbers:
    print(f'O número três apareceu na {numbers.index(3)+1}º posição.')
else:
    print(f'O valor 3 não foi digitado.')
print(f'Os números pares digitados foram: ', end='')
for c in numbers:
    if c % 2 == 0:
        print(f'{c} ', end='')
