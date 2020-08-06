# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('\033[1;30mInforme a velocidade atual do carro: \033[m'))
if v > 80:
    print('\033[31mVocê foi multado por excesso de velocidade!')
    multa = (v-80) * 7
    print('O valor da multa será: R${:.2f}\033[m'.format(multa))
else:
    print('\033[32mBom dia! Continue odedecendo as leis de trânsito\033[m')
