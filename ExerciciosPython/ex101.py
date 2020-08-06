# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

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
