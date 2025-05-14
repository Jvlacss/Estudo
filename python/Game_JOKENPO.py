from random import randint

itens = ('pedra', 'papel', 'tesoura')
print('Digite a sua opção:')
print(''' 
[ 1 ] pedra
[ 2 ] papel
[ 3 ] tesoura
''')
opção = int(input('Qual é a sua jogada? '))
computador = randint(1, 3)

print(f'Computador jogou {itens[computador - 1]}')
print(f'Jogador jogou {itens[opção - 1]}')

if opção == computador:
    print('Empate')
elif (opção == 1 and computador == 3) or (opção == 2 and computador == 1) or (opção == 3 and computador == 2):
    print('Jogador vence')
else:
    print('Computador vence')