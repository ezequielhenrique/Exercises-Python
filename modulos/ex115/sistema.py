from time import sleep

from modulos.ex115.lib.arquivo import *

arq = 'lista.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    criarArquivo(arq)

while True:
    op = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas',  'Sair do sistema'])
    if op == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif op == 2:
        # Opção cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif op == 3:
        # Opção de encerrar o sistema
        cabecalho('ENCERRANDO O SISTEMA... ATÉ LOGO!')
        break
    else:
        # Digitou uma opção errada no menu
        print('\033[31m[ERRO] Digite uma opção válida\033[m')
    sleep(2)
