# Programa que lê um número e mostra seu fatorial

n = int(input('Fatorial do número: '))          # Da pra resolver com o módulo math (factorial)
resultado = 0
c = fatorial = n
print('Calculando {}! = '.format(n), end='')
if n == 0:
    resultado = 1
elif n == 1:
    resultado = 1
else:
    while c > 0:
        print('{}'.format(c), end='')
        print(' x ' if c > 1 else ' = ', end='')
        c -= 1
        fatorial *= c
        if c == 1:
            resultado = fatorial
'''for c in range(n, 0, -1):
    fatorial *= c
    if c == 1:
        resultado = fatorial'''
print(f'{resultado}')
