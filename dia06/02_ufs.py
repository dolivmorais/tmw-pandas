# %%

import pandas as pd


url = pd.read_csv("../data/unidades_federativas.csv",sep=",")
uf = url
# %%

def str_to_float(x):
    x = (x.replace(" ","")
        .replace(",",".")
        .replace("\xa0","")
        .replace(" anos","")
        .replace("anos",""))
    return float(x)

# %%
uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)
uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(str_to_float)
uf
# %%
def uf_to_regiao(uf):

    # tartar uf
    # uf = uf

    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas","Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
       return "Norte"
    elif uf in ["Espírito Santo","Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"
    
uf["Regiao"] = uf["Unidade federativa"].apply(uf_to_regiao)
uf
# %%

# Mortalidade infantil (2016)
# IDH (2010)
# PIB (2015)
def mortalidade_to_float(x:str):
    x = (x.replace("‰","")
         .replace(",",".")
         .replace("	","")
         .replace("\t",""))
    return float(x) 

uf["Mortalidade infantil (/1000)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_float)
uf
# %%
"""
se pib per capit for > de 30k e 
+ mortalidade < de 15 por 1000 + idh > de 700, então parece bom senão não parece bom
"""
def classifca_bom(linha):
    return( linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (/1000)"] < 15 and
            linha["IDH (2010)"] > 700)

# %%
uf.apply(classifca_bom, axis=1)
# %%
