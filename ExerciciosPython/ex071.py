print('=' * 40)
print('Caixa Eletrônico'.center(40))
print('=' * 40)
saq = int(input('Qual valor você deseja sacar? R$ '))
print('-' * 40)
total = saq
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
