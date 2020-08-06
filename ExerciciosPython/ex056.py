# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
# do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

nome = sexo = ''
idade = soma_idade = 0
h_maioridade = 0        # Homem de maior idade
m_menorq20 = 0          # Mulheres com idade menor que 20
h_velho = ''            # Nome do homem mais velho

for c in range(1, 5):
    print('-' * 5, f'{c}º pessoa', '-' * 5)
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()

    soma_idade += idade             # Calcula a soma de todas as idades
    if c == 1 and sexo == 'M':
        h_maioridade = idade
        h_velho = nome
    if sexo == 'M' and idade > h_maioridade:
        h_maioridade = idade
        h_velho = nome
    if sexo == 'F' and idade < 20:
        m_menorq20 += 1

print('-' * 30)
print('A média de idade do grupo é de {:.1f} anos'.format(soma_idade/4))
print(f'O homem de maior idade é {h_velho} com {h_maioridade} anos')
print(f'Há {m_menorq20} mulher(es) com idade menor que 20')
