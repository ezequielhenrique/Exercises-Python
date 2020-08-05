# Lista com valores únicos

num = []
while True:
    v = int(input('Digite um número inteiro: '))
    if len(num) == 0:
        num.append(v)
        print('Valor adcionado com sucesso!')
    else:
        if v in num:
            print('Valores duplicados não podem ser adicionados!')
        else:
            num.append(v)
            print('Valor adcionado com sucesso!')
    cont = ' '
    while cont != 'S' and cont != 'N':
        cont = str(input('Deseja continuar (S/N): ')).strip().upper()[0]
    if cont == 'N':
        break
num.sort()
print('-' * 40)
print(f'Você digitou os valores {num}')
