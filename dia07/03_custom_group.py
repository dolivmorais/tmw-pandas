# %%

import pandas as pd
import numpy as np

transacoes = pd.read_csv('../data/transacoes.csv',sep=";")
transacoes
# %%

def dif_amp(x:pd.Series):
    amplititude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplititude-media)**2)

idades = pd.Series([21,32,25,51,42,23,27,52,32,15])
dif_amp(idades)
# %%
(transacoes.groupby(by=["IdCliente"])
            .agg({
                "IdTransacao": ['count'],
                "QtdePontos": ['sum','mean', dif_amp]
            }))
# %%
