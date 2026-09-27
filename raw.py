# 3.  Estruturação dos dados brutos recebidos pela API da NASA, 
# criando uma classe 'Asteróide' com os tópicos que queremos, 
# para achatar e validar os dados de cada asteroide

from datetime import date
from pydantic import BaseModel, Field, ValidationError

class Asteroide(BaseModel):         #Cria uma classe 'Asteroide' para verificar o formato dos dados recebidos
  data : date
  id : int
  nome : str
  diametro_min_km  : float = Field(ge=0, description = 'Diâmetro maior ou igual a 0')
  diametro_max_km  : float = Field(gt=0, description =  'Diâmetro maior que 0')
  distancia_km : float = Field(ge=0, description =  'Distância maior ou igual a 0')
  velocidade_km_s  : float = Field(gt=0, description = 'Velocidade maior que 0')
  perigoso : bool

    # conta asteroides lidos, pra conferir com element_count

def processar_dados(raw_data_objects):
    total_asteroides = 0
    asteroides = []
    erros = 0

    for data, lista in raw_data_objects.items():
        for a in lista:
            total_asteroides += 1
            aproximacoes = a["close_approach_data"]

            if not aproximacoes:    # lista vazia
                erros += 1
                print(f"Asteroide {a.get('id')} sem dados de aproximação")
                continue

            for aproximacao in aproximacoes:    # uma linha por aproximação
                try:
                    asteroide = Asteroide(
                        id=a["id"],
                        data=aproximacao["close_approach_date"],
                        nome=a["name"],
                        diametro_min_km=a["estimated_diameter"]["kilometers"]["estimated_diameter_min"],
                        diametro_max_km=a["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                        perigoso=a["is_potentially_hazardous_asteroid"],
                        velocidade_km_s=aproximacao["relative_velocity"]["kilometers_per_second"],
                        distancia_km=aproximacao["miss_distance"]["kilometers"])
                    asteroides.append(asteroide)
                except (ValidationError, KeyError) as e:
                    erros += 1
                    print(f"Asteroide {a.get('id')} inválido: {e}")

    return total_asteroides, asteroides, erros