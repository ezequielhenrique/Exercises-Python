# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:

pessoas18 = mulheres20 = homens = 0
while True:
    print('-' * 40)
    print('Cadastre uma pessoa')
    print('-' * 40)
    sexo = cont = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MmFf':
        sexo = str(input('Sexo (M/F): ')).strip().upper()[0]
    if idade >= 18:
        pessoas18 += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres20 += 1
    while cont not in 'SsNn':
        cont = str(input('Quer continuar (S/N): ')).strip().upper()[0]
    if cont in 'Nn':
        break
print(f'''Total de pessoas com mais de 18 anos: {pessoas18}
Total de homens cadastrados: {homens}
São {mulheres20} mulheres com menos de 20 anos''')
