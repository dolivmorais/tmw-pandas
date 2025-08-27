# %%

import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv",sep=";")
df.head()

# %%
df["pontos100"]= df["QtdePontos"] + 100
df
# %%
nova_coluna = []
for i in df["QtdePontos"]:
    nova_coluna.append(i+100)

nova_coluna

# %%
df["emailTwitch"] = df["FlEmail"] + df["FlTwitch"]
df.head()
# %%
df["FlEmail"] * df["FlTwitch"]
# %%
df["qtde_social"] = df["FlEmail"]+ df["FlTwitch"]+ df["FlYouTube"]+ df["FlBlueSky"]	+ df["FlInstagram"]
df
# %%
df["todas_social"] = df["FlEmail"] * df["FlTwitch"] * df["FlYouTube"] * df["FlBlueSky"]	 * df["FlInstagram"]
df
# %%
df["QtdePontos"].describe()
# %%
df["logpontos"]= np.log(df["QtdePontos"]+1)
df["logpontos"].describe()
# %%

import matplotlib.pyplot as plt

plt.hist(df["logpontos"])
plt.show()
# %%
