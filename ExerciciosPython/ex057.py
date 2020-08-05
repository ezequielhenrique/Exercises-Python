# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

s = ''
while s != 'M' and s != 'F':
    s = str(input('Digite o sexo da pessoa (M/F): ')).upper()
    if s != 'M' and s != 'F':
        print('Texto inválido, tente novamente.')
print('FIM')
