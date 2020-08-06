# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.


def escreva(txt):
    c = len(txt) + 6
    print('~' * c)
    print(f'{txt:^{c}}')
    print('~' * c)


escreva('Python')
escreva('Curso em video')
escreva('Dev')
