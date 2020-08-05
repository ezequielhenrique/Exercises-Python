# Crie um programa que leia uma frase qualquer e diga se ela é um
# palíndromo, desconsiderando os espaços.

txt = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(txt)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if junto == inverso:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo')
