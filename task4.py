import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('base.xlsx')

#convertendo para formato de data correto
df['Date Date'] = pd.to_datetime(df['Date Date'])

#Adicionando coluna year

df['Year'] = pd.DatetimeIndex(df['Date Date']).year

#Agrupando os dados por loja e ano, e contando o número de pedidos em cada grupo:
grouped = df.groupby(['Store Name', 'Year'])['Order Number'].count().reset_index()

#criando gráfico com a biblioteca Seaborn

fig, ax = plt.subplots(figsize=(12, 8))
ax = sns.barplot(x='Store Name', y='Order Number', hue='Year', data=grouped)
ax.set_title('Total de pedidos por loja em 2022 e 2023')
ax.set_xlabel('Loja')
ax.set_ylabel('Número de pedidos')
plt.show()