maiores = 0 
menores = 0 

for contador in range(5):
    idade = int(input(f'digite a  idade da {contador + 1 } pessoa: '))
    if idade >= 18:
        print('maior de idade')
        maiores += 1
    else:
        print('menor de idade')
        menores += 1
print(f'temos {maiores} pessoas maiores de idade')
print(f'temos {menores} pessoas menores de idade')