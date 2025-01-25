print('Olá, tudo bem?, seja bem vindo')
nome = str(input('Qual é o seu nome? ')) 
anos = int(input('em quantos anos você deseja pagar:  '))
salario = float(input('Qual é o seu salário? '))
casa = float(input('Qual é o valor da casa? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
if prestacao <= minimo:
    print(f'Parabéns {nome}, seu empréstimo foi aprovado')
    print(f'Você pagará {prestacao:.2f} por mês')
else: 
    print(f'Infelizmente {nome}, seu empréstimo foi negado')