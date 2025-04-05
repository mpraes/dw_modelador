# DW Modelador

A Python-based data warehouse modeling automation tool that uses AI agents to generate complete DW solutions from requirements specifications.

**This project is still in development...**

### 🎯 Features
Automated data warehouse design from text requirements
Multi-agent architecture using CrewAI framework
Generates complete technical artifacts:
Logical data models
ETL/ELT pipelines (dbt, Airbyte)
Infrastructure plans
Technical validation reports
Built-in HTML report generation
Local LLM support via Ollama

### 🏗️ Architecture
Uses crewai for agent orchestration
Specialized agents:
Analista - Requirements analysis
Modelador - Data modeling
Infraestrutura - Infrastructure planning
EngenheiroDataPipeline - Pipeline engineering
Validador - Technical validation

### 🚀 Getting Started
Clone the repository
Install dependencies:

```bash
pip install crewai langchain
```

Create a .env file with your configurations
Place your requirements in requisitos.md
Run the project:

```bash
python main.py
```

```markdown
### 📂 Project Structure

```
.
├── agentes/           # AI agent definitions
├── inputs/            # Input requirements
├── outputs/           # Generated artifacts
├── tasks/             # Agent tasks
├── utils/             # Helper utilities
└── main.py            # Main orchestration
```

### 📄 Generated Outputs
modelo_logico.html - Logical data model
plano_infra.html - Infrastructure plan
pipelines.html - Data pipeline definitions
parecer_validacao.html - Validation report
dashboard.html - Final consolidated report

### 🛠️ Technologies
Python
CrewAI
Ollama (Local LLMs)
dbt
Airbyte
Airflow

### 📝 License
MIT License