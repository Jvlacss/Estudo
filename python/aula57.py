''' n = 1 
par = impar = 0
while n != 0:
    n = int(input('digite um numero: '))
    if n !=  0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')'''



sexo = str(input('digite o seu sexo [M/F]: ')).strip().upper()[10]
while sexo not in 'MF':
    sexo = str(input('digite o seu sexo corretamente [M/F]:    ')).strip().upper()
print('sexo registrado.')