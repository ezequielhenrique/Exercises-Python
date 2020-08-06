# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
# de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[031m[ERRO] por favor, digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('Programa interrompido pelo usuário')
        else:
            return n


def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('\033[031m[ERRO] por favor, digite um número real válido\033[m')
        except KeyboardInterrupt:
            print('Programa interrompido pelo usuário')
        else:
            return n


num1 = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {num1} e o real {num2}')
