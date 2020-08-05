from modulos.ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception as erro:
        print(f'Houve um erro na criação do arquivo/ {erro}')
    else:
        print('Arquivo criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except Exception as erro:
        print(f'Erro ao ler o arquivo/ {erro}')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for lin in a:
            dado = lin.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except Exception as erro:
        print(f'Houve um erro ao abrir um arquivo/ {erro}')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except Exception as erro:
            print(f'Houve um erro ao guardar os dados/ {erro}')
        else:
            print(f'Novo registro {nome} adcionado')
            a.close()
