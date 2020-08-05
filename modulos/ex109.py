from modulos.myModulos import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')
print(f'O dobro de {moedas.moeda(p, "$")} é {moedas.dobro(p)}')
print(f'Aumentando 20% temos {moedas.aumentar(p, 20, False)}')
print(f'Diminuindo 25% temos {moedas.diminuir(p, 25, True)}')
