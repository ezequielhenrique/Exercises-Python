n = c = soma = 0
while n != 999:         # 999 é a condição de parada
    n = int(input('Digite um número inteiro (999 para parar): '))
    if n != 999:
        soma += n
        c += 1
print('Foram digitados {} números e a soma entre eles foi {}.'.format(c, soma))
