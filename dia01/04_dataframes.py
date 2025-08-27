# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

nomes = [
    "a", "a", "c", "d", "e",
    "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o",
]

series_idades = pd.Series(idades)
series_nome = pd.Series(nomes)
#%%
df = pd.DataFrame()
df
#%%
df ["idade"] = series_idades
df ["nomes"] = series_nome
df
#%%
df.iloc[0]["nomes"]
#%%
df.iloc[-1]["nomes"]

# %%
