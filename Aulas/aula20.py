def contador(*num):
    t = len(num)
    print(f'Recebi os valores {num} e são ao todo {t} números.')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# Programa Principal
contador(4, 5)
contador(8, 9, 3, 4)
contador(4, 3, 9, 5, 1, 7)

valores = [3, 5, 10, 2, 9]
dobra(valores)
print(valores)
