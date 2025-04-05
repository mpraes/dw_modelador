from crewai import Task
from utils.output_writer import salvar_html

def validacao_final(agent):
    return Task(
        description="""
Valide se os arquivos gerados para o projeto de pipelines de dados estão consistentes com os requisitos.

Você deve:
- Acessar os arquivos nas pastas:
    - outputs/dbt/schema.yml
    - outputs/dbt/dim_empresa.sql
    - outputs/airbyte/source_postgres.json
    - outputs/airflow/dag_receita_dw.py
- Verificar se cada arquivo existe e possui conteúdo válido
- Validar se cada bloco está estruturado corretamente
- Gerar um parecer técnico com checklist e recomendações

🔸 Checklist esperado:
✅ Arquivo existe  
✅ Sintaxe ou estrutura correta  
✅ Referência a modelos ou funções do projeto (`ref`, `source`, etc)  
✅ Descrição e testes em YAML  
✅ JSON completo  
✅ DAG com operadores válidos

🔸 Formato da resposta:
Use blocos <pre><code class="language-txt"> para cada verificação.
Indique resultado com ✅ ou ❌.
""",
        expected_output="Checklist técnico de conformidade dos arquivos gerados.",
        agent=agent,
        callback=lambda output: salvar_html(
            titulo="Parecer de Validação Final",
            conteudo=getattr(output, "response", str(output)),
            path="outputs/parecer_validacao.html"
        )
    )
