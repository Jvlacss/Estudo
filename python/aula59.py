n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

opcao = 0
maior = 0 
while opcao != 5:
    print('''
    [1]  somar
    [2]  multiplicar
    [3]  maior
    [4]  novos numeros
    [5]  sair do programa  
    ''')
    opcao = int(input('Digite a sua opção:  '))
    if opcao == 1:
        print(f'a soma dos valores é {n1 + n2}')
    elif opcao == 2:
        print(f' a multiplicação dos valores é igual a {n1 * n2}')
    elif opcao == 3:
       elif opcao == 3:
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    print(f'O maior valor apresentado é {maior}')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5: 
        print('Você saiu do programa, volte mamando. ')
    else:
        print('opção errada, my friend.')