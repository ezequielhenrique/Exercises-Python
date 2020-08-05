num = int(input('Digite um número inteiro: '))
div = 0
for c in range(1, num+1):
    if num % c == 0:            # Conta a quantidade de divisores
        div += 1
if div == 2:
    print('{} possui {} divisores portanto é um número primo.'.format(num, div))
else:
    print('{} possui {} divisores portanto não é um número primo.'.format(num, div))
