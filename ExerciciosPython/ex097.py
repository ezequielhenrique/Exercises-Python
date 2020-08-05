def escreva(txt):
    c = len(txt) + 6
    print('~' * c)
    print(f'{txt:^{c}}')
    print('~' * c)


escreva('Python')
escreva('Curso em video')
escreva('Dev')
