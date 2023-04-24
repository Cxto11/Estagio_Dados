import pandas as pd

df = pd.read_excel('base.xlsx')

#convertendo para formato de data correto
df['Date Date'] = pd.to_datetime(df['Date Date'])

#filtrar apenas as linhas que correspondem ao mercado preço baixo e ao mês de dezembro:
df_filtered = df.loc[(df['Store Name'] == 'Mercado Preço Baixo') & (df['Date Date'].dt.month == 12)]

#contar quantos usuários únicos fizeram pedidos no mercado preço baixo:

num_users = df_filtered['User Phone Number'].nunique()

print(f"O número de usuários únicos que fizeram pedidos no mercado Preço baixo em dezembro é {num_users}.")