def vota(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos:', end=' ')
    if idade < 16:
        return 'Não vota!'
    elif 16 <= idade < 18 or idade >= 65:
        return 'Voto opcional!'
    else:
        return 'Voto obrigatório!'


nasc = int(input('Digite seu ano de nascimento: '))
print(vota(nasc))
