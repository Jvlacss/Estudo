n = int(input('Digite o primeiro  NUMERO: '))
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(f'{i}', end=' ' )