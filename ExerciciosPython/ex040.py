# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('REPROVADO')
elif 5 <= m <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
