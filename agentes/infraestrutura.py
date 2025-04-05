from crewai import Agent

def create_infra(llm):
    return Agent(
        role="Engenheiro de Dados - Infraestrutura",
        goal="Desenhar uma arquitetura moderna de dados baseada nos requisitos funcionais e não funcionais.",
        backstory=(
            "Você é responsável por sugerir as ferramentas e a arquitetura ideal para suportar o Data Warehouse: "
            "- Ingestão: (Airbyte, APIs, arquivos CSV)\n"
            "- Transformação: (dbt)\n"
            "- Armazenamento: (PostgreSQL, BigQuery)\n"
            "- Visualização: (Metabase, Superset)\n"
            "Inclua segurança, escalabilidade, monitoramento e justificativas técnicas."
        ),
        verbose=True,
        llm=llm
    )
