lanche = ('Lasanha', 'Pizza', 'Hambúrguer', 'Macarrão', 'Suco', 'Batata Frita')
# Tuplas são imutáveis
for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]}, na posição {c}')
print('>>>')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('>>>')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('>>>')
print(sorted(lanche))
