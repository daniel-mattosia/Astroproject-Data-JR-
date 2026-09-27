# 4. Agora vira DataFrame e vamos remover duplicados, limpar etc

import pandas as pd
from turtle import pd


def criar_dataframe(asteroides):
    df = pd.DataFrame([a.model_dump() for a in asteroides])
    df["data"] = pd.to_datetime(df["data"])
    df.drop_duplicates(subset=["id", "data"], inplace=True)  # remove duplicados
    df.sort_values(by=["data", "distancia_km"], inplace=True)  # ordena por data e distância    

    return df

#print("     DataFrame com todos asteróides do período selecionado\n", df.head())
#df.info()
#print(df.head())
#print(asteroides)
#print(len(df), erros, dados["element_count"])   # df + erros deve bater com element_coun


# Quantidade de asteroides por dia
#print('\n                Asteróides por dia\n',df.groupby('data').size())

# Os 5 mais próximos da Terra
#print('\n#                Asteróides mais Próximos\n', df.nsmallest(5, 'distancia_km')[['data', 'nome', 'distancia_km']])

# Os 5 mais rápidos
##print('\n#                Asteróides mais Rápidos\n', df.nlargest(5, 'velocidade_km_s')[['data', 'nome', 'velocidade_km_s']])

# Quantos são potencialmente perigoso
#print('\n                Potencialmente perigosos\n',df[df['perigoso']][['data','nome', 'distancia_km', 'velocidade_km_s', ]])