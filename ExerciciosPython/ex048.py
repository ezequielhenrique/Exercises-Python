soma = 0
cont = 0
for c in range(1, 500):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
        cont += 1
print('''A soma de todos os {} número ímpares e divisores de 3
no intervalo de 1 até 500 é {}'''.format(cont, soma))
