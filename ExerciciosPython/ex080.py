# Lista ordenada sem repetições

num = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > num[len(num)-1]:
        num.append(n)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Valor adicionado na posição {pos}...')
                break
            pos += 1
print(f'Os valores digitados em oredem foram {num}')
