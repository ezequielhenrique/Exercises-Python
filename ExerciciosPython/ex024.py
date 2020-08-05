# Crie um programa que leia o nome de uma cidade diga se ela começa ou
# não com o nome "SANTO".

nome = str(input('Digite o nome de sua cidade: ')).split()
print('Sua cidade começa com a palavra "Santo"? {}'.format('Santo' == nome[0].title()))
