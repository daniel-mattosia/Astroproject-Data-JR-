# 🌠 NASA Near-Earth Asteroids Data Pipeline

Ferramenta de linha de comando (CLI) em Python que consulta a API da NASA para buscar dados de **NEOs (Near-Earth Objects)** — asteroides que passam próximos da Terra — dentro de um intervalo de datas informado pelo usuário, valida e estrutura os dados, e os armazena de forma organizada em um banco de dados local.

## 📌 Sobre o projeto

O programa recebe duas datas via terminal, consulta a [NeoWs API da NASA](https://api.nasa.gov/), valida as informações recebidas com **Pydantic**, organiza tudo em uma tabela com **pandas**, e salva o histórico em um banco **SQLite** — evitando duplicatas entre execuções diferentes.

Este projeto foi desenvolvido como exercício prático de:
- Consumo de APIs REST
- Validação de dados com Pydantic
- Manipulação de dados com pandas
- Persistência de dados com SQLite
- Boas práticas de organização de código Python (separação em módulos)
- Gerenciamento seguro de credenciais (variáveis de ambiente)

## 🚀 Funcionalidades

- ✅ Validação do intervalo de datas informado (formato, limites, intervalo máximo de 7 dias — limite da própria API da NASA)
- ✅ Requisição à API da NASA com tratamento de erros (status code, timeout)
- ✅ Estruturação e validação dos dados de cada asteroide via modelo Pydantic
- ✅ Contagem de registros lidos, válidos e inválidos
- ✅ Organização dos dados em DataFrame: remoção de duplicados, ordenação por data e distância
- ✅ Formatação amigável de colunas (notação científica, booleanos traduzidos)
- ✅ Armazenamento incremental em banco SQLite, sem duplicar dados já salvos

## 🗂️ Estrutura do projeto

```
astroproject/
├── main.py            # Ponto de entrada — orquestra todo o pipeline
├── datas.py           # Validação do intervalo de datas
├── nasa.py            # Requisição à API da NASA
├── raw.py             # Modelo Pydantic + processamento dos dados brutos
├── organization.py    # Criação, formatação e persistência do DataFrame
├── .env                # Chave da API (não versionado)
└── requirements.txt    # Dependências do projeto
```

## 🛠️ Tecnologias utilizadas

- Python 3
- [requests](https://pypi.org/project/requests/) — requisições HTTP
- [pydantic](https://docs.pydantic.dev/) — validação de dados
- [pandas](https://pandas.pydata.org/) — manipulação de dados tabulares
- [python-dotenv](https://pypi.org/project/python-dotenv/) — variáveis de ambiente
- sqlite3 — banco de dados local (biblioteca padrão do Python)

## ⚙️ Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/astroproject.git
cd astroproject
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Obter uma chave de API da NASA

Crie sua chave gratuita em [https://api.nasa.gov/](https://api.nasa.gov/) (formulário rápido, chave gerada na hora).

### 4. Configurar o arquivo `.env`

Na raiz do projeto, crie um arquivo chamado `.env` com o seguinte conteúdo:

```
NASA_API_KEY=sua_chave_aqui
```

> ⚠️ O arquivo `.env` não deve ser enviado ao GitHub — ele já está incluído no `.gitignore`.

### 5. Executar

```bash
python main.py --inicio 2026-05-01 --fim 2026-05-07
```

## 📋 Exemplo de saída

```
Essas são foram as datas selecionadas: 2026-05-01 até 2026-05-07
API Conectada com sucesso! Dados sendo processados...

        data       id            nome  distancia_formatada(km)  ...  perigoso
0 2026-05-01  3092303    (2001 MS3)                1.21 × 10^7  ...       Não
1 2026-05-01  3631851   (2013 EL28)                5.82 × 10^7  ...       Não
2 2026-05-02  3723888    (2015 NU2)                6.94 × 10^7  ...       Sim
...

33 novos asteroides salvos (0 já existiam).
```
## 📚 Objetivos de Aprendizado

Este projeto está sendo desenvolvido como um projeto prático de portfólio para consolidar conhecimentos em:

* Python;
* APIs REST;
* JSON;
* Pydantic;
* Pandas;
* SQL;
* PostgreSQL;
* ETL;
* Modelagem de dados;
* Pipelines de dados;
* Visualização de dados;
* Git e GitHub.

## 🔮 Possíveis melhorias futuras

- Visualização gráfica dos dados (distância x tempo, quantidade por dia)
- Logging estruturado em vez de `print`
- Testes automatizados (pytest)
- Interface web simples (Streamlit ou Flask)


## 🔭 Roadmap

* [x] Implementar entrada de datas via terminal
* [x] Validar intervalo de datas
* [x] Integrar com a API da NASA
* [x] Processar JSON bruto
* [x] Validar dados com Pydantic
* [x] Criar DataFrame com Pandas
* [ ] Implementar PostgreSQL
* [ ] Implementar carga dos dados
* [ ] Garantir idempotência do pipeline
* [ ] Criar consultas SQL para análise
* [ ] Criar visualizações interativas
* [ ] Documentar o pipeline completo

## 📄 Licença

Este projeto está sob a licença MIT.

## Autor
**Nome:** Daniel Mattos

**Perfil:** Estudante universitário | Candidato a vaga Júnior em Engenharia de Dados
