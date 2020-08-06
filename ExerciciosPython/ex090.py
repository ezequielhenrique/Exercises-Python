# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
elif aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Aprovado'
print('-' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
