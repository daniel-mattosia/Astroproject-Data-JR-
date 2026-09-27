#Consulta as datas fornecidas e faz a requisição a API da NASA para obter 
# os dados dos objetos próximos da Terra (NEOs) dentro do intervalo de datas especificado.  
import requests, os
import datetime

API_URL = "https://api.nasa.gov"
API_KEY = os.getenv("API_KEY")  # Carrega a chave da API do arquivo .env

def request_api(endpoint : str,
                api_key : str,
                params : dict,
                timeout : int = 10):

  url = f"{API_URL}{endpoint}"
  query_params = {"api_key": api_key}

  if params:
        query_params.update(params)

  response = requests.get(url, params=query_params, timeout=timeout)
  if response.status_code == 200:
        return response.json()
  else:
        raise SystemExit(f"Erro na API: {response.status_code} - {response.text[:200]}")


def buscar_dados(data_inicial, data_final):
     dados = request_api("/neo/rest/v1/feed", API_KEY, params={ "start_date": data_inicial.isoformat(),
                                                          "end_date": data_final.isoformat()}) 
     raw_data_objects = dados["near_earth_objects"]
     return raw_data_objects  