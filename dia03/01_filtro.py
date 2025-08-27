# %%

import pandas as pd

# %%
# com for
pontos = [1,2,3,4,5]
lista = []
for i in pontos:
    if i > 3:
        lista.append(i)
lista       
# %%
pontos = [1,2,3,4,5]
filtro = []

lista = []
for i in pontos:
    filtro.append(i> 3)
filtro

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])
resultado


#%%
# istconprehension
pontos = [1,2,3,4,5]
lista = [i for i in pontos if i > 3]
lista
# %%
brinquedo = pd.DataFrame(
    {
        "nome": ["boneco", "boneco", "boneco", "boneco", "boneco", "boneco"],
        "idade": [12,21,13,14,25,16],
        "uf:":  ["SP","SP", "AC", "AP" ,"RJ", "SP"]
    }
)

filtro = brinquedo["idade"] >= 20
brinquedo[filtro]
# %%
df = pd.read_csv("../data/transacoes.csv",sep=";")

# %%
filtro = df["QtdePontos"] >= 50 
df[filtro]

# %%
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
df[filtro]
#%%
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 50)
df[filtro]
# %%
