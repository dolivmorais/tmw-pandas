# %%
# 06.04 - Quem teve mais transações de Streak?

import pandas as pd

# %%

transacoes = pd.read_csv("../../data/transacoes.csv",sep=";")
transacoes.head()

# %%
transacao_produto = pd.read_csv("../../data/transacao_produto.csv",sep=";")
transacao_produto.head()

# %%
produtos = pd.read_csv("../../data/produtos.csv",sep=";")
produtos.head()

# %%

cliente_transacao_produto = transacoes.merge(
    transacao_produto,
    on="IdTransacao",
    how="left",
)[['IdTransacao', "IdCliente", "IdProduto"]]

df_full = cliente_transacao_produto.merge(
    produtos,
    left_on=['IdProduto'], right_on=['IdProduto'],
    how='left',
)

df_full = df_full[df_full["DescProduto"]=="Presença Streak"]

(df_full.groupby(by=["IdCliente"])["IdTransacao"]
        .count()
        .sort_values(ascending=False)
        .head(1)
)
df_full
# %%

produtos = produtos[produtos["DescProduto"]=="Presença Streak"]

(transacoes.merge(transacao_produto, on=["IdTransacao"], how="left")
           .merge(produtos, on=["IdProduto"], how="inner")
           .groupby(by="IdCliente")["IdTransacao"]
           .count()
           .sort_values(ascending=False)
           .head(5)
)
# %%

