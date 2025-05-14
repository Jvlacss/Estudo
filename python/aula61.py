'''print('=-=-=-=' * 2, 'PA', '=-=-=-=-' * 2)
a1 = int(input('Primeiro Termo:   '))
r = int(input('Digite a razão da PA(r): '))

termo = a1
cont = 1 
while cont <= 10:
    print(f'{termo}  ', end= ' ')
    termo += r
    cont += 1
print('CABOU')'''


a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

while True:
    termo = a1 
    cont = 1 

    while cont <= 10:
        print(f'{termo} >', end=' ')
        termo += r
        cont += 1
    print('PAUSA')

    print('''
[1] Continuar 
[2] Parar
''')
    opcao = int(input('Digite a sua opção: ')) 

    if opcao == 1:
        a1 = int(input('Digite o novo primeiro termo: '))
        r = int(input('Digite a nova razão: '))
    elif opcao == 2:
        print('Fim do programa, bye!')
        break
    else:
        print('Opção invalida, cabou programa.')
        break
print(f'A progressão foi finalizada com {termo} exibidos, uii')


