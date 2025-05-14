num1 = int(input('Digite a primeira nota: '))
num2 = int(input('Digite a segunda nota: '))
media = (num1 + num2) / 2

if media >= 7:
    print('você foi aprovado 😃')
elif media >= 5 and media < 7:
    print('você está de recuperação')
else:
    print('você foi reprovado')