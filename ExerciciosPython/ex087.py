# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma = maior = 0
for li in range(0, 3):
    for c in range(0, 3):
        matriz[li][c] = int(input(f'Digite um número para a posição [{li},{c}]: '))
for li in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[li][c]:^5}]', end='')
        if matriz[li][c] % 2 == 0:
            pares += matriz[li][c]
        if c == 2:
            soma += matriz[li][c]
        if li == 1:
            if c == 0:
                maior = matriz[li][c]
            else:
                if matriz[li][c] > maior:
                    maior = matriz[li][c]
    print()
print('-' * 40)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')
