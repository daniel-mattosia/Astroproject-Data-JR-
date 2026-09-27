# 4. Agora vira DataFrame e vamos remover duplicados, limpar etc
import pandas as pd
import sqlite3

def formatar_notacao_cientifica(numero, casas_decimais=2):
            # Formata um número em notação científica com a quantidade de casas decimais especificada
    if numero == 0:
        return "0"
    expoente = int(f"{numero:e}".split("e")[1])
    mantissa = numero / (10 ** expoente)
    
    return f"{mantissa:.{casas_decimais}f} × 10^{expoente}"

def converte_bool(valor):
            # Converte valores booleanos em "Sim" ou "Não" para exibição no DataFrame
    return "Sim" if valor else "Não"

def criar_dataframe(asteroides):
                     #Converte cada objeto pydantic em um dicionário
                     #comum do Python pra cada asteroide da lista
    dados = []
    for asteroide in asteroides:
        dados.append(asteroide.model_dump())

    df = pd.DataFrame(dados) 
    return df

def formartar_dataframe(df):

        #Formata o DataFrame, convertendo a coluna, removendo duplicados e resetando o índice

    df["data"] = pd.to_datetime(df["data"])                             #Converte data de string para datetime
    df.drop_duplicates(subset=["id", "data"], inplace=True)             #Remove duplicados por id e data
    df.reset_index(drop=True, inplace=True)                             #Reset index do DataFrame

    return df

def salvar_no_banco(df):

            # Salva o DataFrame no banco de dados SQLite, removendo duplicados com base em id e data

    conexao = sqlite3.connect("asteroides.db")
    try:
        df_existente = pd.read_sql("SELECT id, data FROM asteroides", conexao)
        ja_existe = df.set_index(["id", "data"]).index.isin(
            df_existente.set_index(["id", "data"]).index)
        df_novo = df[~ja_existe]
    except pd.errors.DatabaseError:
        df_novo = df    

    df_novo.to_sql("asteroides", conexao, if_exists="append", index=False)
    conexao.close()
    return df_novo

def exibir_dataframe(df):
        # Exibe o DataFrame formatado, com colunas de distância e velocidade em notação científica 
        # e coluna de perigoso como "Sim" ou "Não"

    df_exibicao = df.copy()
    df_exibicao["perigoso"] = df_exibicao["perigoso"].apply(converte_bool)
    df_exibicao["distancia_formatada(km)"] = df_exibicao["distancia_km"].apply(formatar_notacao_cientifica) #Converte a coluna de distância em notação científica
    df_exibicao["velocidade_formatada(km/s)"] = df_exibicao["velocidade_km_s"].apply(formatar_notacao_cientifica) #Formata a coluna de velocidade em notação científica
    
    df_exibicao = df_exibicao.drop(columns=["distancia_km", "velocidade_km_s"]) #Remove as colunas de distância e velocidade originais
    
    return df_exibicao