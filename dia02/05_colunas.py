# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv",sep=";")
df


# %%
df.shape
# %%
df.info(memory_usage="deep")
# %%
df.dtypes
# %%
# renomear colunas
df = df.rename(columns={
                        "IdTransacao": "id_transacao",
                        "DtCriacao": "qtde_pontos",
                        "DtCriacao": "dt_criacao",})
df
# %%
df.columns
# %%
# acessando colunas
df[["IdCliente","QtdePontos"]]
# %%
colunas = list(df.columns)
colunas.sort()
colunas
# %%
df[colunas]
df
# %%
