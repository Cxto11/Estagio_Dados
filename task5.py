import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('base.xlsx')

#convertendo para formato de data correto
df['Date Date'] = pd.to_datetime(df['Date Date'])

#Adicionando coluna year

df['Year'] = pd.DatetimeIndex(df['Date Date']).year

#Agrupamento de dados por loja e ano, contando p número de pedidos únicos em cada grupo:

grouped = df.groupby(['Store Name', 'Year'])['Order Number'].nunique().reset_index()

df2 = pd.pivot_table(grouped, values='Order Number', index='Store Name', columns='Year')

#variação percentual de pedidos únicos de cada loja entre os anos:
df2['Variação %'] = (df2[2023] - df2[2022]) / df2[2022] * 100

print(df2)