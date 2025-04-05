from crewai import Task
from utils.output_writer import salvar_html

def modelagem_dados(agent):
    return Task(
        description="""
Crie um modelo lógico de dados para um Data Warehouse com base nos requisitos fornecidos.
Você deve seguir boas práticas de modelagem dimensional, utilizando estrutura em estrela.

🔸 INSTRUÇÕES:
- Use <pre><code class="language-sql"> para formatar blocos de código SQL
- Nomeie tabelas com prefixo `dim_` para dimensões e `fato_` para tabelas fato
- Defina colunas, tipos e chaves primária/estrangeira
- Separe dimensões: empresa, estabelecimento, sócio, cnae, simples
- Se possível, inclua uma tabela fato relacionada (ex: registro ou movimentação)

🔸 EXEMPLO DE FORMATAÇÃO:
<pre><code class="language-sql">
CREATE TABLE dim_empresa (
  cnpj_base CHAR(8) PRIMARY KEY,
  razao_social VARCHAR(255)
);
</code></pre>
""",
        expected_output="Modelo lógico formatado em SQL com destaque HTML, seguindo padrão de DW.",
        agent=agent,
        callback=lambda output: salvar_html(
            titulo="Modelo Lógico de Dados",
            conteudo=getattr(output, "response", str(output)),
            path="outputs/modelo_logico.html"
        )
    )
