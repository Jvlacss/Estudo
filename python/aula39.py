from datetime import date
atual = date.today().year

ano = int(input('ano de nascimento: '))
print (f'Quem nasceu em {ano} tem {atual - ano} anos em {atual}, e;\n')
idade = atual - ano
if idade == 18:
    print('Você precisa se alistar imediatamente')
if idade < 18:
    print(f'Você ainda não precisa se alistar, faltam {18 - idade} anos')
    print(f'Seu alistamento será em {ano + 18}')
if idade == 19:
    print(f'Você já deveria ter se alistado há {idade - 18} ano, será refrátario')
elif idade > 20:
    print(f'se você não se alistou, você está em atraso de {idade - 18} anos, e pode ser preso') 
        