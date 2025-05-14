numero = int(input("Digite um número: "))
rollin = str(input('Quer continuar a digitar números? [S/N]')).strip().upper()
soma = quant = media = maior = menor = 0
while rollin == 'S':
    numero += int(input("Digite um número: "))
    rollin = str(input('Quer continuar a digitar números? [S/N]')).strip().upper()
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    if rollin == 'N':
        break
print(f'A soma dos números digitados é {numero}')
print(f'voce digitou {quant} números e a média foi {numero/quant}')









