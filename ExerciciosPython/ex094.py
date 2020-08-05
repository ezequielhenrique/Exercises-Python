grupo = list()
pessoas = dict()
mulheres = list()
while True:
    pessoas['nome'] = str(input('Nome: ')).strip()          # Pergunta o nome
    pessoas['sexo'] = str(input('Sexo (M/F): ')).strip().upper()[0]     # Pergunta o sexo
    while pessoas['sexo'] != 'M' and pessoas['sexo'] != 'F':      # Pede novamente o sexo, caso seja digitado errado
        print('[ERRO] Responda com M ou F!')
        pessoas['sexo'] = str(input('Sexo (M/F): ')).strip().upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    if pessoas['sexo'] == 'F':                  # Se for mulher adciona na lista de mulheres
        mulheres.append(pessoas['nome'])
    grupo.append(pessoas.copy())            # Adciona a pessoa cadastrada a uma lista
    op = ' '
    while op != 'S' and op != 'N':          # Pergunta se deseja continuar
        op = str(input('Deseja continuar? ')).strip().upper()[0]
        if op != 'S' and op != 'N':
            print('[ERRO] Responda com S ou N!')
    if op == 'N':
        break
print('=*=' * 20)
print(f'A) Ao todo são {len(grupo)} pessoas cadastradas.')
soma = 0
for c in range(0, len(grupo)):      # Soma a idade de todas as pessoas cadastradas
    pessoa = grupo[c]
    soma += pessoa['idade']
media = soma / len(grupo)
print(f'B) A média de idade é de {media:.1f}')
print(f'C) As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(f'{m};', end=' ')
print(f'\nD) Lista das pessoas que estão acima da média:')
for c in range(0, len(grupo)):          # Varre os elementos da lista
    pessoa = grupo[c]                   # Adciona o elemento a uma variável
    if pessoa['idade'] >= media:         # Verifica se a idade da pessoa é maior que a média
        for k, v in pessoa.items():     # Exibe os dados da pessoa
            print(f' {k} = {v};', end=' ')
        print()
print()
print('-' * 25, 'PROGRAMA ENCERRADO', '-' * 25)
