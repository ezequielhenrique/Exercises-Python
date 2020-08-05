# Validando expresssões matemáticas

exp = str(input('Digite uma expressão matrmática: '))
par1 = exp.count('(')
par2 = exp.count(')')
if par1 == par2:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
