# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
# ele disser que quer mostrar 0 termos.

print('-' * 5, '10 Termos de uma Progressão Aritimética (v3.0)', '-' * 5)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
tot_termos = 0
mais_termos = 10
while mais_termos != 0:
    tot_termos += mais_termos
    while c <= tot_termos:
        print('{} -> '.format(termo), end='')
        c += 1
        termo += razao
    print('Pausa')
    mais_termos = int(input('Você deseja mostrar mais quantos termos (0-nenhum)? '))
print('-' * 50)
print('Progessão finalizada com {} termos mostrados.'.format(tot_termos))
print('Programa Encerrado')
