# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()
leves = list()
pesadas = list()
cont = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    op = ' '
    while op != 'S' and op != 'N':
        op = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
    if op == 'N':
        break
for p in pessoas:
    if cont == 0:
        maior = menor = p[1]
        leves.append(p[0])
        pesadas.append(p[0])
    else:
        if p[1] == maior:
            pesadas.append(p[0])
        if p[1] == menor:
            leves.append(p[0])
        if p[1] > maior:
            pesadas.clear()
            maior = p[1]
            pesadas.append(p[0])
        if p[1] < menor:
            leves.clear()
            menor = p[1]
            leves.append(p[0])
    cont += 1
print('-' * 100)
print(pessoas)
print(f'Ao todo você cadastrou {cont} pessoas.')
print(f'O maior peso foi {maior}Kg, peso de {pesadas}.')
print(f'O menor peso foi {menor}Kg, peso de {leves}')
