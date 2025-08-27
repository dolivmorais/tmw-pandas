# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df

# %%
# salvar
df.to_csv("clientes.csv", index=False)
# %%
df.to_parquet("clientes.parquet")
# %%
df3 = df.to_excel("clientes.xlsx",index=False)
df3
# %%
