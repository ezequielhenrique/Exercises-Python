from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 9:
    print('O atleta possui {} anos e pertence a categoria mirim.'.format(idade))
elif idade <= 14:
    print('O atleta possui {} anos e pertence a categoria infantil.'.format(idade))
elif idade <= 19:
    print('O atleta possui {} anos e pertence a categoria junior.'.format(idade))
elif idade <= 20:
    print('O atleta possui {} anos e pertence a categoria senior.'.format(idade))
else:
    print('O atleta possui {} anos e pertence a categoria master.'.format(idade))
