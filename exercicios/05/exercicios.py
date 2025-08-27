# %%

import pandas as pd
import numpy as np

# %%
# 05.01 - Crie uma coluna nova “twitch_points” que á
# resultado da multiplicação do saldo de pontos e a marcação da twitch

clientes = pd.read_csv("../../data/clientes.csv")

clientes["twitch_points"] = clientes["qtdePontos"] * clientes["flTwitch"]
clientes.head()

# %%
# 05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova

clientes["logPontos"] = np.log(clientes["qtdePontos"])
clientes.head()

# %%
# 05.03 - Crie uma coluna que sinalize se a
# pessoa tem vínculo com alguma (qualquer uma)
# plataforma de rede social.
clientes["ao_menos_uma_social"] = clientes["flTwitch"] + clientes["flYouTube"] + clientes["flBlueSky"] + clientes["flInstagram"]
clientes.head()

# 05.04 - Qual é o id de cliente que tem maior saldo de pontos?
# E o menor?

clientes.sort_values(by="qtdePontos", ascending=False).head(1)["idCliente"]

clientes.sort_values(by="qtdePontos", ascending=True).head(1)["idCliente"]

# %%
# 05.05 - Selecione a primeira transação diária de cada cliente.

import pandas as pd

transacoes = pd.read_csv("../../data/transacoes.csv")
transacoes.head()

transacoes["data"] = pd.to_datetime(transacoes["dtCriacao"]).dt.date
transacoes = transacoes.sort_values("dtCriacao")

# %%

first = transacoes.drop_duplicates(keep="first", subset=["idCliente", "data"])
last = transacoes.drop_duplicates(keep="last", subset=["idCliente", "data"])

pd.concat([last, first])