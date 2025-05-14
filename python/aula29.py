num = int(input('Digite o número para conversão: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] Binário')
print('[ 2 ] Octal')
print('[ 3 ] Hexadecimal')
opcao = int(input('Digite a sua opção: '))

if opcao == 1:
    print(f'{num} convertido para binário é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Opção inválida!')