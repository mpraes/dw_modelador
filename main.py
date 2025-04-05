import os
from crewai_tools import FileReadTool
from utils.llms import get_llms
from utils.dashboard_generator import gerar_dashboard
from utils.file_split_writer import salvar_multiplos_arquivos
from utils.output_writer import salvar_html

# === Importação dos agentes ===
from agentes.analista import create_analista
from agentes.modelador import create_modelador
from agentes.infraestrutura import create_infra
from agentes.engenheiro_pipelines import create_pipelines_engineer
from agentes.validador import create_validador

# === Importação das tasks ===
from tasks.analise_requisitos import analise_requisitos
from tasks.modelagem_dados import modelagem_dados
from tasks.infra_setup import infra_setup
from tasks.pipeline_engenharia import engenharia_pipelines
from tasks.validacao_final import validacao_final

# === LLMs ===
llms = get_llms()

# === Ferramentas ===
file_tool = FileReadTool()

# === Criação dos agentes ===
analista = create_analista(llms["analista"], file_tool)
modelador = create_modelador(llms["modelador"])
infra = create_infra(llms["infra"])
pipelines = create_pipelines_engineer(llms["pipelines"])
validador = create_validador(llms["validador"])

# === Execução sequencial ===

# 1. Analista de Requisitos
print("🔍 Etapa 1: Análise de Requisitos")
task_analista = analise_requisitos(analista)
output_analista = task_analista.execute_sync()
analista_context = getattr(output_analista, "response", str(output_analista))

# 2. Modelagem de Dados
print("📐 Etapa 2: Modelagem de Dados")
task_modelador = modelagem_dados(modelador)
task_modelador.context = analista_context
output_modelador = task_modelador.execute_sync()
modelador_context = getattr(output_modelador, "response", str(output_modelador))

# 3. Infraestrutura
print("🏗️ Etapa 3: Infraestrutura")
task_infra = infra_setup(infra)
task_infra.context = analista_context
output_infra = task_infra.execute_sync()
infra_context = getattr(output_infra, "response", str(output_infra))

# 4. Engenharia de Pipelines
print("🔄 Etapa 4: Engenharia de Pipelines")
task_pipelines = engenharia_pipelines(pipelines)
task_pipelines.context = f"""
Modelo Lógico:
{modelador_context}

Plano de Infraestrutura:
{infra_context}
"""
output_pipelines = task_pipelines.execute_sync()
pipelines_context = getattr(output_pipelines, "response", str(output_pipelines))

# === Separação dos arquivos gerados pelo engenheiro de pipelines ===
salvar_multiplos_arquivos(
    conteudo=pipelines_context,
    pasta_base="outputs"
)

# Função utilitária para leitura segura de arquivos
def ler_arquivo(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return f"❌ Arquivo não encontrado: {path}"

# 5. Validação Final
print("✅ Etapa 5: Validação Final")
conteudo_dbt_sql = ler_arquivo("outputs/dbt/dim_empresa.sql")
conteudo_dbt_yml = ler_arquivo("outputs/dbt/schema.yml")
conteudo_airbyte = ler_arquivo("outputs/airbyte/source_postgres.json")
conteudo_airflow = ler_arquivo("outputs/airflow/dag_receita_dw.py")

task_validador = validacao_final(validador)
task_validador.context = f"""
📁 Conteúdo real dos arquivos para validação técnica:

🟣 dbt/schema.yml
<pre><code class="language-yaml">
{conteudo_dbt_yml}
</code></pre>

🟣 dbt/dim_empresa.sql
<pre><code class="language-sql">
{conteudo_dbt_sql}
</code></pre>

🔵 airbyte/source_postgres.json
<pre><code class="language-json">
{conteudo_airbyte}
</code></pre>

🟢 airflow/dag_receita_dw.py
<pre><code class="language-python">
{conteudo_airflow}
</code></pre>
"""
output_validador = task_validador.execute_sync()
validador_context = getattr(output_validador, "response", str(output_validador))

# === Dashboard final (opcional) ===
gerar_dashboard({
    "modelo_logico": "outputs/modelo_logico.html",
    "plano_infra": "outputs/plano_infra.html",
    "parecer_validacao": "outputs/parecer_validacao.html",
    "pipelines": "outputs/pipelines.html"
})

# Resultado final no terminal
print("\n✅ Resultado do validador:")
print(validador_context)
