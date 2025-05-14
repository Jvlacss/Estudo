#teste
soma = 0 
cont = 0 
for i in range(1, 50, 2):
    print(i, end=' ')
    if i % 3 == 0:
        soma = soma  + i 
        cont = cont + 1
print(f'\nA soma de todos os  {cont} valores solicitados é {soma}')
#teste
