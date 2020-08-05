print('-' * 10, 'Cáuculo de IMC', '-' * 10)
peso = float(input('Qual seu peso(kg)? '))
altura = float(input('Qual a sua altura(m)? '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Seu imc é de {:.2f} você está abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu imc é de {:.2f} você está com peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('Seu imc é de {:.2f} você está com sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Seu imc é de {:.2f} você está com obesidade'.format(imc))
else:
    print('Sei imc é de {:.2f} você está com obesidade mórbida'.format(imc))
