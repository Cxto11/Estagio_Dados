import pandas as pd

# carregando a tabela em um DataFrame
df = pd.read_excel('base.xlsx')

# filtrando os dados da loja Mercado Marisol
df_marisol = df[df['Store Name'] == 'Mercado Marisol']

# convertendo a coluna "Orden aprobada" em valores binários
df_marisol['Orden aprobada (Yes / No)'] = df_marisol['Orden aprobada (Yes / No)'].map({'Yes': 1, 'No': 0})

# agrupando os dados pelo mês e calculando a média de "Orden aprobada"
df_marisol_mes = df_marisol.groupby(df_marisol['Date Date'].dt.month)['Orden aprobada (Yes / No)'].mean().reset_index()

# ordenando os dados em ordem decrescente de percentual de rejeição
df_marisol_mes = df_marisol_mes.sort_values(by='Orden aprobada (Yes / No)', ascending=False)

# selecionando o primeiro registro (que contém o mês com o maior percentual de rejeição)
mes_maior_rejeicao = df_marisol_mes.iloc[0]['Date Date']

print(mes_maior_rejeicao)