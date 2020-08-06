# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça
# também um programa que importe esse módulo e use algumas dessas funções.

from modulos.myModulos import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p:.2f} é R${moedas.metade(p):.2f}')
print(f'O dobro de R${p:.2f} é R${moedas.dobro(p):.2f}')
print(f'Aumentando 10% temos R${moedas.aumentar(p, 10):.2f}')
print(f'Diminuindo 15% temos R${moedas.diminuir(p, 15):.2f}')
