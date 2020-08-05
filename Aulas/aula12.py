nome = str(input('Qual é o seu nome: '))
if nome == 'Ezequiel':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Pedro' or nome =='Paulo':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))
