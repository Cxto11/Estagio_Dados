import pandas as pd

# lê o arquivo Excel
df = pd.read_excel("base.xlsx")

#Filtrar os dados da loja Super Baratão no mês de dezembro:
filtro = (df['Store Name'] == 'Super Baratão') & (df['Date Date'].dt.month == 12)


dados_filtrados = df[filtro]

#Contar o número de pedidos que tiveram apenas um item vendido:
pedidos_com_um_item = dados_filtrados[dados_filtrados['Quantity Itens'] == 1]['Order Number'].nunique()


print(pedidos_com_um_item)