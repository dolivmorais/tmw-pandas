import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

# Define um cabeçalho para "fingir" ser um navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36"
}

# Faz a requisição
response = requests.get(url, headers=headers)
response.raise_for_status()  # lança erro se não conseguir baixar

# Lê as tabelas do HTML
dfs = pd.read_html(response.text)

#print(len(dfs))        # mostra quantas tabelas encontrou
#print(dfs[0].head())   # exibe as primeiras linhas da primeira tabela

df_uf = dfs[1]
df_uf.to_csv("unidades_federativas.csv", index=False)
