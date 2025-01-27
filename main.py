import pandas as pd
import matplotlib.pyplot as plt

vendas_loja = pd.read_csv("vendas_loja.csv")

vendas_loja = vendas_loja.fillna(0)

vendas_loja["Receita"] = vendas_loja["Quantidade"] * vendas_loja["Preco_Unitario"]

total_receita = vendas_loja["Receita"].sum()

total_quantidade = vendas_loja["Quantidade"].sum()

#3 categorias mais vendidas em termos de receita
top3_categorias = (
vendas_loja.groupby("Categoria")["Receita"].sum().sort_values(ascending=False).head(3)
)

receita_por_categoria = vendas_loja.groupby("Categoria")["Receita"].sum()
receita_por_categoria.plot(kind ="bar",title = "Receita Total por Categoria")
plt.xticks(rotation=360)
plt.xlabel("Categoria")
plt.ylabel("Receita")
plt.show()


produto_mais_vendido = (vendas_loja.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False).idxmax())

receita_produto_mais_vendido = (vendas_loja[vendas_loja["Produto"]==produto_mais_vendido]["Receita"].sum())
# Convertendo para datetime e extraindo o mês
vendas_loja["Data"] = pd.to_datetime(vendas_loja["Data"])
vendas_loja["Mes"] = vendas_loja["Data"].dt.month
receita_por_mes = vendas_loja.groupby("Mes")["Receita"].sum()

# Gráfico de receita por mês
receita_por_mes.plot(kind="line", title="Receita Total por Mês", marker="o")
plt.xlabel("Mês")
plt.ylabel("Receita")
plt.show()


# Tarefa 7: Insights Finais
print("\n### Insights Finais ###")
print(f"Total de receita gerada: R$ {total_receita:.2f}")
print(f"Quantidade total de produtos vendidos: {total_quantidade}")
print("Três categorias mais vendidas (em receita):")
print(top3_categorias)
print(f"Produto mais vendido: {produto_mais_vendido}")
print(f"Receita do produto mais vendido: R$ {receita_produto_mais_vendido:.2f}")
print("Receita total por mês:")
print(receita_por_mes)










