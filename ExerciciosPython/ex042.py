r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
if abs(r2-r3) < r1 < r2 + r3 and abs(r1-r3) < r2 < r1 + r3 and abs(r1-r2) < r3 < r1 + r2:
    print('As retas formam um triângulo', end='')
    if r1 == r2 == r3:
        print(' equilátero.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print(' isósceles.')
    else:
        print(' escaleno.')
else:
    print('As retas não formam um triângulo')
