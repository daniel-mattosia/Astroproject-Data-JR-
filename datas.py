#Recebe datas passadas no terminal e transforma no formato que a API requisita  
import argparse
from datetime import datetime   


def pegar_datas():
    
    # Função para pegar as datas de início e fim do usuário.
   
    parser = argparse.ArgumentParser()
    parser.add_argument("--inicio", required=True)
    parser.add_argument("--fim", required=True)
    args = parser.parse_args()

    return args.inicio, args.fim

def validar_datas(inicio, fim): 
      
                  # Valida as datas passadas no terminal e 
                  # transforma no formato que a API  requisita
      try:
          data_inicial = datetime.strptime(inicio, "%Y-%m-%d").date()
          data_final = datetime.strptime(fim, "%Y-%m-%d").date()  
      except ValueError:
          raise ValueError("Erro! As datas devem estar no formato AAAA-MM-DD (ex: 2026-10-09).")
      if data_inicial < datetime(1990, 1, 1).date() or data_final < datetime(1990, 1, 1).date():
            raise ValueError("Erro! As datas devem ser maiores que 01/01/1990.")
      if data_inicial > datetime.now().date() or data_final > datetime.now().date():
            raise ValueError("Erro! As datas devem ser menores que a data atual.")
      if data_inicial == data_final:
            raise ValueError("Erro! As datas não podem ser iguais.")
      if data_inicial > data_final:
            raise ValueError("Erro! A data inicial não pode ser maior que a final.")
      if (data_final - data_inicial).days >= 7:
            raise ValueError("Erro! O intervalo máximo é de 7 dias.")
      
      return data_inicial, data_final