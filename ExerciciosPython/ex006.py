# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número inteiro: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de {0} é {1}\nO triplo de {0} é {2}\nA raiz de {0} é {3}'.format(n, d, t, r))
