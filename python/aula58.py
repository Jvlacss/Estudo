from random import randint
''' computador = randint(0, 10)
print('vamos fazer um jogo, estou pensando em um numero de 0 a 10')
acerto = False
palpite = 0 
while not acerto:
    jogador = int(input('digite um numero de 0 a 10:   '))
    palpite += 1 
    if jogador == computador:
        acertou = True
    else: 
        if jogador < jogador:
            print('tente mais uma vez')
        elif jogador > jogador: 
            print('tente mais uma vez')
print(f'acertou com {palpite}')''' 

from random import randint
computador = randint(0, 4)
print('vamos fazer um jogo, estou pensando em um numero de 1 a 4, tente adivinha')
acerto = False 
palpites = 0 
while not acerto:
    jogador = int((input('digite um numero de 1 a 4:   ')))
    
    palpites += 1 

    if jogador == computador:
        acerto = True
    else:
        if jogador >= computador:
            print('muito alto, tente  um numero mais baixo')
        elif jogador < computador:
            print('muito baixo, motherfucker, tente um numero mais alto')
if palpites > 2:
    print('parabéns seu lindo, voce é mui inteligente')
else:
    print(f'você acertou com {palpites}, seu burro.')