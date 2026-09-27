# organization.py
import sqlite3
import pandas as pd

def criar_dataframe(asteroides):
    # ... seu código que já existe ...
    return df

def salvar_no_banco(df):
    conexao = sqlite3.connect("asteroides.db")

    try:
        df_existente = pd.read_sql("SELECT id, data FROM asteroides", conexao)
        ja_existe = df.set_index(["id", "data"]).index.isin(
            df_existente.set_index(["id", "data"]).index
        )
        df_novo = df[~ja_existe]
    except pd.errors.DatabaseError:
        df_novo = df

    df_novo.to_sql("asteroides", conexao, if_exists="append", index=False)
    conexao.close()

    return df_novo