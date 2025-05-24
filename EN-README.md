![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

<p align="right">
  <a href="README.md">
    Portuguese <img src="assets/br.png" width="16" alt="br_flag">
  </a>
</p>

<a href="https://www.flaticon.com/free-icons/etl" title="etl icons">
  <img align="left" alt="etl" height="45" width="45" src="./assets/etl.png">
</a>

# SIMPLE MODULAR ETL PIPELINE WITH TESTS AND LOGS

## ABOUT THE PROJECT

This project primarily focuses on the standardized construction of project structure and documentation, as a secondary aspect, **with less concern for ETL sophistication**, it presents a business problem and the challenge of improving the process by implementing a modular ETL pipeline in Python, divided into three main stages:

- Extract: reading and concatenating multiple Excel files.
- Transform: data cleaning and normalization, export to Parquet.
- Load: reading Parquet and final export to Excel.

Strict attention has been paid to project structure and documentation.  
After each stage, the pipeline performs unit tests with `pytest`.  
At the end, it performs an integration test that validates the global success! 🚀

All events are logged in a file automatically generated in the `docs/` folder.  
The file records all pipeline stages and unit test results, with the following naming format:  
`docs/log_YYYYMMDD_HHMMSS.log`.

## PIPELINE FLOW

- Extract → Test, if ok:
- Transform → Test, if ok:
- Load → Test, if ok:
- Final Test ✅
- Log generated 📄
- END 🎯

## BUSINESS PROBLEM

### Context:

Currently, companies in sectors such as retail, healthcare, or logistics need to consolidate data from various sources (spreadsheets, legacy systems, APIs, databases). This integration is often performed manually, through fragile and costly processes, making it difficult to properly map information and increasing the risk of inconsistencies.

These challenges negatively impact the organization's ability to align data with strategic business requirements, such as:

- Achieving operational efficiency.
- Improving data quality.
- Supporting predictive and prescriptive analyses.
- Complying with regulatory requirements.

Therefore, how can we automate the integration and validation of data from multiple sources to support business strategy in a reliable, fast, and automated way, promoting cost-effectiveness and improving operational and tactical decision-making functions, thereby adding value to decisions?

### How Your Solution Addresses This Problem:

The project automates the extraction of these files, transforms the data with specific business rules (e.g., date adjustments, category standardization), separates the final result by sectors, and stores it in Parquet format, additionally, the solution includes automated tests to validate the transformations before loading, achieving the following results:

🔹 The business area now receives updated reports daily, when the data consolidation time is reduced by 80%.

🔹 Data Mapping:  
Your solution performs data reading, transformation, and standardization, allowing the identification, mapping, and consolidation of dispersed information.  
This enables the creation of a structured data inventory, facilitating traceability and compliance with security and privacy standards.

🔹 Automation Aligned with Strategy:  
The automation of the pipeline, with unit tests and continuous integration, reduces dependence on manual processes.  
This supports the organization's digital transformation strategy, promoting scalability and agility in delivering insights to business areas.

🔹 Value Addition:  
By transforming data into optimized formats (such as Parquet), your solution enables faster and more efficient analyses.  
This adds value not only by reducing operational costs but also by providing more accurate and timely information for decision-making.

🔹 Requirement Identification and Compliance:  
The modular structure (extract, transform, load) allows quality, security, and performance requirements to be clearly defined, tested, and validated.  
Automated tests with Pytest ensure that transformations follow business rules, guaranteeing reliability in deliveries.

---

## GETTING STARTED

### Prerequisites

1. Git and GitHub: Used for code versioning and as the project's remote repository.  
You must have Git installed on your machine and also have an account on GitHub.  
[Git installation instructions here](https://git-scm.com/doc).  
[GitHub installation instructions here](https://docs.github.com/en).

2. Pyenv: Used to manage Python versions in virtual environments, essential for isolating the application and avoiding conflicts between library versions and Python itself.  
[Pyenv installation instructions here](https://github.com/pyenv/pyenv#installation).  
In this project, we will use Python 3.11.4.

3. Poetry: This project uses Poetry for dependency management.  
[Poetry installation instructions here](https://python-poetry.org/docs/#installation).

### File Structure

The basic file structure for the project is organized as follows:

```bash
📦 jornada_workshop01
├── 📁 app
│   └── 📁 pipeline
│       ├── extract.py
│       ├── transform.py
│       └── load.py
├── 📁 assets
│   └── brazil.png
│   └── etl.png
│   └── us.png
├── 📁 data
│   ├── 📁 input
│   └── 📁 output
│       ├── concatenated_data.parquet
│       └── files_loaded.xlsx
├── 📁 docs
│   └── 📁 logs
│       └── log_YYYYMMDD_HHMMSS.txt
├── 📁 tests
│   ├── test_extract.py
│   ├── test_transform.py
│   ├── test_load.py
│   └── test_pipeline.py
├── .gitignore
├── README.md
├── pytest.ini
├── pyproject.toml
└── main.py
```

---

### Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/andrematiello/jornada_workshop01
```

2. Access the workshop directory:

```bash
cd jornada_workshop01
```

3. Set up the correct Python version:

```bash
pyenv install 3.11.4
```

4. Set the local Python version for the project:

```bash
pyenv local 3.11.4
```

5. Configure Poetry to use Python 3.11.4:

```bash
poetry env use 3.11.4
```

6. To create the virtual environment, since version 2 of Poetry, according to the official documentation, the Poetry Shell is not included by default and must be installed as a dependency Poetry Docs (https://python-poetry.org/docs/managing-environments/#powershell):

```bash
poetry self add poetry-plugin-shell
```

7. To activate the virtual environment:

```bash
poetry shell
```

8. Update the lock file precisely and immutably with all dependencies and their versions, including sub-dependencies, in the `poetry.lock` file:

```bash
poetry lock
```

9. Install the project dependencies (without packaging the project) using the following command, as specified in the `pyproject.toml` file:

```bash
poetry install --no-root
```

---

### How to run the project:

1. Execute the pipeline:

```bash
python -m app.main
```

2. Check in the `data/output` folder if the file was generated correctly. 

3. Check in the `docs/logs` folder if the log file was generated correctly, according to the ETL's date and time. 

---

### How to run individual tests:

1. Test for data extraction (extract):

```bash
pytest tests/test_extract.py
```

2. Test for data transformation (transform):

```bash
pytest tests/test_transform.py
```

3. Test for data loading into Excel and .parquet format files (load):

```bash
pytest tests/test_load.py
```

4. Test the entire pipeline:

```bash
pytest tests/test_pipeline.py
```

### How to run all tests at once:

```bash
pytest
```

---

## TECHNOLOGIES USED

- Python 3.11+, official documentation: https://www.python.org/ 
- Pyenv, official documentation: https://pypi.org/project/pyenv-win/ 
- Poetry, official documentation: https://pypi.org/project/poetry/
- Git and GitHub, official documentation: https://git-scm.com/ and https://github.com/

## LIBRARIES USED

- Pandas: for data manipulation, official documentation: https://pypi.org/project/pandas/  
- Pyarrow: for reading and writing in Parquet format, official documentation: https://pypi.org/project/pyarrow/  
- Pytest: for automated testing, official documentation: https://pypi.org/project/pytest/  
- Numpy: a library for performing numerical calculations and large-scale data manipulation, official documentation: https://pypi.org/project/numpy/  
- Blue: for adopting best practices according to Pep8, official documentation: https://pypi.org/project/blue/  
- Ignr: for automated pre-creation of the .gitignore file, official documentation: https://pypi.org/project/ignr/  

## DOCUMENTATION

Run the following command to view the project documentation:

```bash
task doc
```

---

## ABOUT THE DATA

### SIMPLE CLEANING AND TRANSFORMATIONS WERE PERFORMED

Through an orchestrator function `transform_data`, all steps are executed in the following order:

🔹 Name standardization: prevents typos and column name inconsistencies, also facilitates future manipulations and analyses.  
🔹 Removal of rows with NaN: ensures that the dataset does not have incomplete data and avoids errors in functions that do not accept NaN values.  
🔹 Removal of name prefixes: makes names cleaner for analyses, reports, and visualizations, avoiding grouping or duplication errors caused by different formatting.  
🔹 Separation of date and time: facilitates separate temporal analyses: by date, time, weekday, etc., and prepares the dataset for potential derived columns.  
🔹 Salary formatting: makes the dataset ready for presentation or reports and improves understanding and readability for stakeholders.  
🔹 Conversion of numerics to float: ensures that all numeric columns (int64, float64) are converted to float.  
🔹 Normalization of numerics (except excluded ones): avoids errors in mathematical operations and is essential for some functions like normalization.  

## COMMENTS

### Now you have:

🔹 A robust pipeline;  
🔹 Intermediate tests;  
🔹 Complete logs;  
🔹 Top-notch documentation! 😉  

### This project delivers a complete and professional ETL pipeline, following Data Engineering best practices, with a focus on:

🔹 Modularity: each step separated with a single responsibility: Extract, Transform, and Load.  
🔹 Testability: automated tests with Pytest at each step, ensuring code quality and safe evolution.  
🔹 Observability: structured logging system, with automatic generation of log files identified by date and time, allowing complete traceability of each execution.  
🔹 Automation: sequential and validated execution of the entire process, with immediate stop in case of failure, avoiding error propagation.  
🔹 Clear documentation: objective guidelines on execution, project structure, and data flow, facilitating maintenance and scalability.  
🔹 Aesthetics and usability: enriched with emojis and friendly messages to make execution more visual and intuitive.  

---

## MAIN TECHNICAL FEATURES

### 🔒 Security and Control:

Automated validation of each step via unit tests with Pytest, ensuring that failures are identified and handled immediately and in a controlled manner.  
Through a defensive architecture, the pipeline automatically stops execution in case of error, avoiding the propagation of inconsistencies.

### 🛠️ Robustness and Scalability:

Modular structure oriented to specific functions, ensuring maintainability and ease of extension for new requirements or integrations.  
Structured logging, with execution timestamps and status of each step, enabling complete traceability and facilitating audits.

### 📊 Observability and Transparency:

All events and operations are recorded in persistent logs, automatically generated and stored in `docs/`, allowing a clear view of execution and supporting compliance and forensic processes.

### 🚀 Value Delivery:

Automation of the entire ETL flow: from ingestion to the export of processed and validated data, with explicit guarantees of quality and reliability, through risk mitigation with intermediate tests, avoiding the delivery of corrupted or incomplete data.  
Preparation of data in optimized formats (Parquet and Excel), ready for analysis, reporting, or integration with Business Intelligence systems.  

---

Project inspired by Workshop 01 of the Data Journey, with adaptations;  
Project carried out with the support of Artificial Intelligence (ChatGPT);  
For future improvements: extraction of real data with cleaning and transformation, followed by loading into a Data Warehouse, possibly in a cloud provider. Also, an ETL orchestrated with Apache Airflow and best CI/CD practices.

## QUESTIONS, SUGGESTIONS OR FEEDBACK

#### 🚀 André Matiello C. Caramanti - [matiello.andre@hotmail.com](mailto:matiello.andre@hotmail.com)

#### "This pipeline not only executes, but validates, records, and ensures data quality from end to end, according to Data Engineering best practices."

---

## LICENSE

[MIT License](https://andrematiello.notion.site/mit-license)
