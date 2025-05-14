somaidade = 0
mediaidade = 0 
maioridadehomem = 0 
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print(f'--------- {p}ª pessoa ---------')
    nome = input('Qual o seu nome? ')
    idade = int(input('Qual a sua idade? '))
    sexo = input('Digite o seu sexo (M/F): ').strip().upper()

    somaidade += idade 

    if sexo == 'M':
        if idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome

    if sexo == 'F' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4

print(f'\nA média de idade do grupo é de {mediaidade:.1f} anos.')
if nomevelho:
    print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
else:
    print('Nenhum homem foi informado.')
print(f'Ao todo são {totmulher20} mulher(es) com menos de 20 anos.')
