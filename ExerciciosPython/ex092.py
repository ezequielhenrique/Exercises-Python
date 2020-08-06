# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule
# e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
trabalhador = dict()
ano_atual = datetime.today().year
trabalhador['Nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
trabalhador['Idade'] = ano_atual - nasc
trabalhador['CTPS'] = int(input('Nº carteira de trabalho (0-não tem): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = int(input('Valor do salário: '))
    trabalhador['Aposentadoria'] = (trabalhador['Contratação'] + 35) - nasc
print('=-=' * 15)
for k, v in trabalhador.items():
    print(f'  -{k} tem o valor {v}')
