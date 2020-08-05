num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para binário
[2] Converter para octal
[3] Converter para hexadecimal''')
base = int(input('Sua opção: '))
if base == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')
