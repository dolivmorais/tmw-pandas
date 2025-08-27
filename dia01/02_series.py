# %%

import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]
media = sum(idades) / len(idades)
print("media:",media) #media

diffs = 0
for i in idades:
    diffs += (i - media)**2

variancia = diffs / (len(idades)-1)
print("variancia:",variancia) #variancia
# %%
series_idades = pd.Series(idades)
series_idades

# %%
media = print(series_idades.mean()) #series_idades.mean()
var_idade = print(series_idades.var()) #series_idades.var()
summary_idades = print(series_idades.describe()) #series_idades.describe()
# %%
