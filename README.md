
# ☄️ NASA Near-Earth Asteroids Data Pipeline
A Data Engineering project that collects, validates, transforms, stores, and analyzes data about Near-Earth Objects (NEOs) using NASA's API.

🇧🇷 [Leia em Português](README-pt-br.md)



## 🎯 Project Goal

Build a data pipeline capable of:

* Receiving a date range through the command line;
* Collecting asteroid data from NASA's NEO API;
* Processing raw JSON data;
* Validating records using Pydantic;
* Transforming the data into a tabular structure using Pandas;
* Storing the processed data in PostgreSQL;
* Performing analysis and SQL queries;
* Creating interactive data visualizations.

## 🔄 Pipeline

```text
Date Input
    ↓
Date Validation
    ↓
NASA NEO API
    ↓
Raw JSON
    ↓
Data Processing & Validation
    ↓
Pydantic
    ↓
DataFrame
    ↓
PostgreSQL
    ↓
Data Analysis
    ↓
Interactive Visualizations
```

## 🛠️ Technologies

* Python
* Requests
* Pydantic
* Pandas
* PostgreSQL
* SQL
* Git
* GitHub
* NASA Near Earth Object API

## 📌 Data Collected

For each asteroid close approach, the pipeline works with information such as:

* Asteroid ID;
* Name;
* Close approach date;
* Minimum estimated diameter;
* Maximum estimated diameter;
* Potentially hazardous classification;
* Relative velocity in km/s;
* Miss distance from Earth in km.

The project uses **one row per close approach**, allowing multiple approaches from the same asteroid to be represented as separate records.

## 🧹 Data Processing

NASA's API returns nested JSON structures. The processing stage extracts the relevant information and converts it into a structured format.

The pipeline also performs:

* Handling of asteroids without close approach data;
* Data validation using Pydantic;
* Handling of missing or unexpected fields;
* Handling of Pydantic `ValidationError` exceptions;
* Tracking of processed records and errors.

## 📊 DataFrame

After processing and validation, the records are converted into a Pandas DataFrame.

The DataFrame represents the structured data layer before persistence in the database.

## 🗄️ Database

**In development**

The next stage of the project is implementing PostgreSQL persistence.

The database design will take into account the project's data grain and use an appropriate unique key to prevent duplicate records when the same period is processed multiple times.

## 📈 Visualizations

**In development**

Interactive visualizations will be created to explore topics such as:

* Number of close approaches over time;
* Potentially hazardous asteroids;
* Closest approaches to Earth;
* Relative velocity;
* Asteroid diameter distribution;
* Close approach trends over time.

## 🚀 How to Run

The project receives the start and end dates through command-line arguments.

Example:

```bash
python main.py --inicio 2026-09-01 --fim 2026-09-07
```

The date range is validated before the API request is performed.

## 📁 Project Structure

```text
projeto_nasa/
│
├── main.py
├── datas.py
├── nasa.py
├── modelos.py
├── transformacao.py
├── requirements.txt
└── README.md
```

The structure may evolve as new pipeline stages are implemented.

## 📚 Learning Objectives

This project is being developed as a practical portfolio project to consolidate knowledge in:

* Python;
* REST APIs;
* JSON;
* Pydantic;
* Pandas;
* SQL;
* PostgreSQL;
* ETL;
* Data modeling;
* Data pipelines;
* Data visualization;
* Git and GitHub.

## 🔭 Roadmap

* [x] Implement command-line date input
* [x] Validate date range
* [x] Integrate with NASA API
* [x] Process raw JSON
* [x] Validate data with Pydantic
* [x] Create Pandas DataFrame
* [ ] Implement PostgreSQL
* [ ] Implement data loading
* [ ] Ensure pipeline idempotency
* [ ] Create SQL analysis queries
* [ ] Create interactive visualizations
* [ ] Document the complete pipeline


## Author

**Name** Daniel Mattos

**Profile:** University Student 

**Candidate** Junior Data Engineering

