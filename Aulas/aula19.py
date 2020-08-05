pessoas = {'nome': 'Ezequiel', 'idade': 18, 'sexo': 'M'}
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['peso'] = 70.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
