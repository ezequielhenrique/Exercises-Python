num = []
for c in range(1, 6):
    num.append(int(input('Digite um valor: ')))
num.append(6)
num.sort(reverse=True)
num.insert(2, 4)
if 10 in num:
    num.remove(10)
else:
    print('Não encontrei o 10')
for p, n in enumerate(num):
    print(f'Na posição {p} encontrei o valor {n}')
num2 = num[:]
num2[2] = 0
print(num2)
