import random 
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')

def game():
    limpa_tela()
    print('\nBem Vindo(a) ao jogo da forca')
    print('Adivinhe a palavra abaixo \n')
    
    #Palavras
    palavras = ['banana',
                'uva',
                'morango',
                'abacaxi',
                'laranha',
                'limao',
                'pera']
    #escolhe a palavra de forma automatica
    palavra = random.choice(palavras)
    #llist comprehesion
    letras_descobertas = [ '_' for letra in palavra]
    #quantidade de chances
    chances = 6 
    letras_erradas = []
    count = 0 
    while chances > 0:
        print(''.join(letras_descobertas))
        print('\n chances restantes: ', chances)
        print('letras erradas', ' '.join(letras_erradas))
        
        #tentativa 
        tentativa = input('\nDigite uma letra: ').lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index]  = letra
                index += 1
        else:
            chances -= 1 
            letras_erradas.append(tentativa)
        #condicional
        if '_' not in letras_descobertas:
            print('\nVoçê venceu, a palavra era:  ', palavra) 
            break   
        #finalização
    if "_"  in letras_descobertas:
        print('\nVoçê perdeu, não há letras restantes')
    #bllocmain
if __name__ == '__main__':
    game()
    print('Parabéns por jogar!')
