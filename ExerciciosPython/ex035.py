# Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuário se elas podem ou não formar um triângulo.

r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
if abs(r2-r3) < r1 < r2 + r3 and abs(r1-r3) < r2 < r1 + r3 and abs(r1-r2) < r3 < r1 + r2:
    print('As retas formam um triângulo!')
else:
    print('As retas não formam um triângulo')
