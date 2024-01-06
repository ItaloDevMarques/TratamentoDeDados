import plotly.express as px
import os
import pandas as pd

# Caminho dos arquivos de vendas
caminho_arquivos = "C:\\Users\\Italo\\Desktop\\Projeto Tratamento de Dados\\Material do projeto\\Vendas"

# Lista de arquivos de vendas
lista_arquivos = os.listdir(caminho_arquivos)

# DataFrame vazio
tabela_total = pd.DataFrame()

# Itera sobre os arquivos de vendas
for arquivo in lista_arquivos:
    # Verifica se o arquivo contém a palavra "Vendas"
    if "Vendas" in arquivo:
        # Lê o arquivo CSV como um DataFrame
        tabela = pd.read_csv(f"{caminho_arquivos}/{arquivo}")
        # Adiciona o DataFrame à tabela total
        tabela_total = pd.concat([tabela_total, tabela], axis=0)

# Exibe a tabela total
print(tabela_total)

# Tabela de produtos mais vendidos
tabela_produtos = tabela_total.groupby("Produto").sum(numeric_only=True)
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)

# Exibe a tabela de produtos mais vendidos
print(tabela_produtos)

# Tabela de faturamento por produto
tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
tabela_faturamento = tabela_total.groupby("Produto").sum(numeric_only=True)
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)

# Exibe a tabela de faturamento por produto
print(tabela_faturamento)

# Tabela de faturamento por loja
tabela_lojas = tabela_total.groupby("Loja").sum(numeric_only=True)
tabela_lojas = tabela_lojas[["Faturamento"]]

# Exibe a tabela de faturamento por loja
print(tabela_lojas)

# Gráfico de faturamento por loja
grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y="Faturamento")

# Exibe o gráfico
grafico.show()
