# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).

nome = str(input('Digite seu nome completo: ')).strip()

print('Nome em maiúsculas: {}'.format(nome.upper()))
print('Nome em minúsculas: {}'.format(nome.lower()))

qespacos = nome.count(' ')          # Conta a quantidade de espaços
caracteres = len(nome)              # Conta a quantidade de caracteres
qletras = caracteres - qespacos
print('O nome possui {} letras'.format(qletras))

div = nome.split()              # Divide o nome em palavras
qletras1 = len(div[0])          # Mostra o número de letras do primeiro nome
print('Nº de letras do primeiro nome: {}'.format(qletras1))
