# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui.

from modulos.myModulos import moedas

p = float(input('Digite um preço: R$ '))
moedas.resumo(p, 20, 30)
