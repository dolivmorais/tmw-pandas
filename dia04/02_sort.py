# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv",sep=';')

clientes = pd.DataFrame(clientes)

max_ponto = clientes["QtdePontos"].max()
print(max_ponto)
filtro = clientes["QtdePontoS"] == max_ponto
clientes[filtro]

# %%

top_5 = (clientes.sort_values(by="QtdePontos", ascending=False)
                 .head(5)["IdCliente"] )

type(top_5)

# %%
clientes

# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario":[2345, 4533, 3245, 4533],
    }
)

brinquedo

# %%

brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])
# %%
