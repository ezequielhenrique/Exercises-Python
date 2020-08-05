# Primeiro e último nome de uma pessoa

nome = str(input('Digite seu nome completo: ')).title().split()
print('Primeiro nome: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))
