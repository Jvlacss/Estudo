from datetime import date

total_maior = 0
total_jovem = 0
total_menor = 0

atual = date.today().year

for pessoa in range(1, 6):
    nascimento = int(input(f'Descreva o ano de nascimento da {pessoa}ª pessoa: '))
    idade = atual - nascimento

    if idade >= 21:
        print('A pessoa é maior de idade')
        total_maior += 1
    elif 18 <= idade < 21:
        print('Esta pessoa é um jovem adulto')
        total_jovem += 1
    else:
        print('Esta pessoa é um menor de idade')   
        total_menor += 1

print(f'\nTotal de pessoas maiores de idade: {total_maior}')
print(f'Total de jovens adultos: {total_jovem}')
print(f'Total de menores de idade: {total_menor}')
