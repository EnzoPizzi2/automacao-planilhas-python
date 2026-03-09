import pandas as pd

# lê a planilha
df = pd.read_excel("vendas.xlsx")

# cria nova coluna com total por item
df["total_item"] = df["quantidade"] * df["preco_unitario"]

# calcula faturamento total
faturamento_total = df["total_item"].sum()

print(f"Faturamento total: R$ {faturamento_total:.2f}")

# salva novo arquivo
df.to_excel("relatorio_vendas.xlsx", index=False)

print("Relatório gerado com sucesso.")
