boletim = list()
aluno = list()
nota = list()
while True:
    aluno.append(str(input('Nome: ')).strip())
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    aluno.append(nota[:])
    boletim.append(aluno[:])
    nota.clear()
    aluno.clear()
    op = ' '
    while op != 'S' and op != 'N':
        op = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
    if op == 'N':
        break
print('=-=' * 20)
print('No. NOME       MÉDIA')
print('-' * 35)
c = 0
for a in boletim:
    print(f'{c:<4}{a[0]:<12}{sum(a[1])/2:.1f}')
    c += 1
print('-' * 35)
while True:
    no = int(input('Deseja mostrar notas de qual aluno (999 para parar)? '))
    if no == 999:
        break
    if no <= len(boletim)-1:
        print('-' * 50)
        print(f'>>>>> Notas de {boletim[no][0]}: {boletim[no][1]}')
print('-' * 20, 'PROGRAMA ENCERRADO', '-' * 20)
