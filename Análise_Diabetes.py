import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe
from google.colab import auth
from oauth2client.client import GoogleCredentials


#conectando ao google drive.
from google.colab import drive
drive.mount('/content/drive')

#trazendo o arquivo do drive ao colab
dados = open("/content/drive/MyDrive/amostras_diabetes_.xlsx", "r", encoding="utf-8")

#definindo o DF (o df é a base para todos os comandos)
caminho = "/content/drive/MyDrive/amostras_diabetes.xlsx"
df = pd.read_excel(caminho)

df.head()

Gravidas	Glicose	Pressão arterial	gordura corporal subcutânea	Insulina	IMC	Situação Corporal	Probalidade Diabetes hereditaria	Idade	Diabetica
0	9	134	74	33	60	25.9	Peso normal	0.460	81	0
1	2	119	0	0	0	19.6	Peso normal	0.832	72	0
2	4	145	82	18	0	31.1	Peso normal	0.235	70	1
3	5	132	80	0	0	26.8	Peso normal	0.186	69	0
4	5	136	82	0	0	0.0	Peso normal	0.640	69	

#Vamos verificar a granularidade de gravidez x idade. com isso veremos primeiro com qual idade nossas mulheres estão tendo alto índice de grávidez.  
df[['Gravidas', 'Idade']]

	Gravidas	Idade
0	9	81
1	2	72
2	4	70
3	5	69
4	5	69
...	...	...
763	1	21
764	0	21
765	1	21
766	0	21
767	2	21
768 rows × 2 columns


# Importanto a biblioteca matplotib e aplicando grafico de dispersão. 
from matplotlib import pyplot as plt
_df_3.plot(kind='scatter', x='Gravidas', y='Idade', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

c:\Users\Pcsam\Downloads\frame1.png

#agora vamos analisar o índice glisemico por idade
df_plot = df[['Idade', 'Glicose']].sort_values(by='Idade')

# Criando  o gráfico
plt.figure(figsize=(8, 4))
plt.plot(df_plot['Idade'], df_plot['Glicose'], marker='o', linestyle='-', color='teal')
plt.title('Glicose por Idade')
plt.xlabel('Idade')
plt.ylabel('Glicose')

# Removendo as bordas superiores e direitas
plt.gca().spines[['top', 'right']].set_visible(False)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

c:\Users\Pcsam\Downloads\frame2.png

# Verificamos que até os 40 anos de idade, o índice glisemico tende a ter a sua máxima em glisemia à 150. 
# Verificamos também que após os 50 anos o a glisemia não segue um padrçao 'convencional' não seguindo uma granularidade e se dispersando. Com isso podemos teremos que analisar um fator importante
# ... após os 50 anos que é o índice corporal e padrão de saúde da 'acolhida'. 

df_plot = df[['IMC', 'Glicose']]

# primeiro preciso categorizar o IMC. 
def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc < 25:
        return 'Peso normal'
    elif imc < 30:
        return 'Sobrepeso'
    elif imc < 35:
        return 'Obesidade grau I'
    elif imc < 40:
        return 'Obesidade grau II'
    else:
        return 'Obesidade grau III'

# depois é necessário aplicar a função ao DataFrame
df['faixa_imc'] = df['IMC'].apply(classificar_imc)

# Agrupar e calcular média de glicose por faixa de IMC
media_glicose = df.groupby('faixa_imc')['Glicose'].mean().reindex([
    'Abaixo do peso',
    'Peso normal',
    'Sobrepeso',
    'Obesidade grau I',
    'Obesidade grau II',
    'Obesidade grau III'
])

# Plotar gráfico
plt.figure(figsize=(10, 6))
media_glicose.plot(kind='bar', color='coral', edgecolor='black')
plt.title('Média de Glicose por Faixa de IMC')
plt.xlabel('Faixa de IMC')
plt.ylabel('Glicose média')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.gca().spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.show() 

c:\Users\Pcsam\Downloads\frame 3.png
