#  Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('A primeira nota do aluno é: '))
nota2 = float(input('A segunda nota do aluno é: '))
m = (nota1+nota2)/2
print('A média do aluno é: {:.2f}'.format(m))
