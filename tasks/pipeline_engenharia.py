from crewai import Task
from utils.file_split_writer import salvar_multiplos_arquivos

def engenharia_pipelines(agent):
    return Task(
        description="""
Você é responsável por construir múltiplos pipelines de ingestão e transformação para um Data Warehouse baseado em dados da Receita Federal.

🔸 Gere os seguintes arquivos:

🟣 Transformações (dbt .sql)
- outputs/dbt/dim_empresa.sql
- outputs/dbt/dim_estabelecimento.sql
- outputs/dbt/dim_socio.sql
- outputs/dbt/dim_simples.sql

🟡 Metadados dbt (schema.yml)
- outputs/dbt/schema.yml → Incluindo todos os modelos acima

🔵 Ingestão via Airbyte (.json)
- outputs/airbyte/source_empresas.json
- outputs/airbyte/source_estabelecimentos.json
- outputs/airbyte/source_socios.json
- outputs/airbyte/source_simples.json

🟢 DAG Airflow
- outputs/airflow/dag_receita_dw.py

🔸 FORMATO DE RESPOSTA (obrigatório):
Delimite cada arquivo com:
---FILENAME--- outputs/dbt/dim_empresa.sql
<conteúdo do arquivo>

---FILENAME--- outputs/dbt/schema.yml
<conteúdo do schema.yml>

🔸 Linguagem por bloco:
- SQL → `<pre><code class="language-sql">`
- YAML → `language-yaml`
- JSON → `language-json`
- Python → `language-python`

Seja técnico, completo e funcional.
""",
        expected_output="Múltiplos arquivos para pipelines reais: SQL, YAML, JSON e Python.",
        agent=agent,
        callback=lambda output: salvar_multiplos_arquivos(
            conteudo=getattr(output, "response", str(output)),
            pasta_base="outputs"
        )
    )
