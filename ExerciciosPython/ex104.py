# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.


def leiaint(txt):
    while True:
        t = input(txt)
        if t.isnumeric():
            n = int(t)
            break
        else:
            print('\033[0;31m[ERRO] Digite um número inteiro!\033[m')
    return n


num = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
