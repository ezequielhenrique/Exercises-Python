# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from modulos.myModulos import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')
print(f'O dobro de {moedas.moeda(p, "$")} é {moedas.dobro(p)}')
print(f'Aumentando 20% temos {moedas.aumentar(p, 20, False)}')
print(f'Diminuindo 25% temos {moedas.diminuir(p, 25, True)}')
