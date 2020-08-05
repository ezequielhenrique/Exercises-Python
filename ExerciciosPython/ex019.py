# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na
# tela o nome do escolhido.

import random
n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
sort = random.choice(lista)
print('O aluno(a) sorteado é: {}'.format(sort))
