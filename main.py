from datas import pegar_datas, validar_datas
from nasa import buscar_dados
from raw import processar_dados
from organization import criar_dataframe, formartar_dataframe, salvar_no_banco, exibir_dataframe

def main():
    
    try:
        inicio, final = pegar_datas()
        inicio, final = validar_datas(inicio, final)
        print(f'Essas são foram as datas selecionadas: {inicio} até {final}')

        raw_data_objects = buscar_dados(inicio, final)
        total_asteroides, asteroides, erros = processar_dados(raw_data_objects)
        print("API Conectada com sucesso! Dados sendo processados...")

        print(f" Total de asteroides lidos: {total_asteroides}\n",
              f"Total de asteroides válidos: {len(asteroides)}\n",
              f"Total de asteroides inválidos: {erros}")

        df = criar_dataframe(asteroides)
        df_novo = formartar_dataframe(df)
        salvar_no_banco(df_novo)
        df_exibicao = exibir_dataframe(df_novo)
        print(df_exibicao.head())

    except ValueError as error:
        print(f"{error}")
        return
      

if __name__ == "__main__":
    main()      