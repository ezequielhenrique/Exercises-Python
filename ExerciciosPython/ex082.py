# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
# três listas geradas.

num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um número inteiro: ')))
    op = ' '
    while op != 'S' and op != 'N':
        op = str(input('Deseja continuar (S/N): ')).strip().upper()[0]
    if op == 'N':
        break
for n in num:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('-' * 40)
print(f'Foram digitados os números: {num}')
print(f'Os número pares são: {pares}')
print(f'Os números ímpares são: {impares}')
