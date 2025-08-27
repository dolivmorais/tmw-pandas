# %%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv",sep=";")
df_clientes

# %%
# mostra N linhas do dataframe
df_clientes.head(3)
# %%
# ver as 5 ultimas linhas (final)
df_clientes.tail(5)

# %%
# sortidos
df_clientes.sample(5)

# %%
# quntidade de linhas e colunas
df_clientes.shape
# %%
# nomr das colunas
colunas = df_clientes.columns
for i,d in enumerate(colunas):
    print(i,d)
# %%
#info fo dataframe
df_clientes.info(memory_usage="deep")
# %%
# tipos de colunas
df_clientes.dtypes

