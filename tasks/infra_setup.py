from crewai import Task
from utils.output_writer import salvar_html

def infra_setup(agent):
    return Task(
        description=(
            "Proponha uma infraestrutura moderna de dados para suportar o data warehouse. "
            "Inclua ferramentas de ingestão (ex: Airbyte), transformação (ex: dbt), orquestração (ex: Airflow) "
            "e armazenamento (ex: PostgreSQL, BigQuery). Justifique cada escolha e explique o fluxo completo."
        ),
        expected_output=(
            "Plano de arquitetura de dados com ferramentas sugeridas e fluxo de dados end-to-end."
        ),
        agent=agent,
        callback=lambda output: salvar_html(
            titulo="Plano de Infraestrutura de Dados",
            conteudo=getattr(output, "response", str(output)),
            path="outputs/plano_infra.html"
        )
    )
