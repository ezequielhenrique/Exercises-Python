# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:


def notas(*nota, sit=False):
    """
    -> Função para analizar nota e situação de vários alunos
    :param nota: Recebe as notas dos alunos (uma ou várias)
    :param sit: Valor opcional, indica se adciona ou não a situação do aluno
    :return: Dicionário com várias informações sobre a situação da turma
    """
    boletim = dict()
    c = maior = menor = soma = 0
    for n in nota:
        if c == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        soma += n
        c += 1
    media = soma / c
    boletim['Total'] = c
    boletim['Maior'] = maior
    boletim['Menor'] = menor
    boletim['Média'] = media
    if sit:
        if media >= 7:
            boletim['Situação'] = 'Boa'
        elif media >= 5:
            boletim['Situação'] = 'Rasoável'
        else:
            boletim['Situação'] = 'Ruim'
    return boletim


resp = notas(9.5, 5.3, 4, 6, 1.5, 10, 10, 9.7, sit=True)
print(resp)

help(notas)
