# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação.

times = ('Sport', 'São Paulo', 'Santos', 'Grêmio', 'Athletico-PR', 'Atlético-MG', 'Vasco',
         'Bragantino', 'Internacional', 'Palmeiras', 'Coritiba', 'Goiás', 'Fortaleza', 'Ceará',
         'Bahia', 'Botafogo', 'Atlético-GO', 'Fluminense', 'Corinthians', 'Flamengo')
print(f'Lista dos times do Brasileirão: {times}')
print(f'Cinco primeiros colocados: {times[:5]}')
print(f'Quatro últimos colocados: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'Posição do Bragantino na tabela: {times.index("Bragantino")+1}º')
