import os
import re

def extrair_conteudo_box(html):
    match = re.search(r'<div class="box">(.*?)</div>', html, re.DOTALL)
    return match.group(1).strip() if match else "<p>Conteúdo não encontrado</p>"

def gerar_dashboard(output_paths, titulo="Relatório Final DW CrewAI", path="outputs/dashboard.html"):
    def ler(p): 
        return extrair_conteudo_box(open(p, encoding="utf-8").read()) if os.path.exists(p) else "<p>Arquivo não encontrado.</p>"

    modelo = ler(output_paths.get("modelo_logico"))
    infra = ler(output_paths.get("plano_infra"))
    parecer = ler(output_paths.get("parecer_validacao"))

    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>{titulo}</title>
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                background: #f8f9fa;
                color: #333;
                margin: 0;
                padding: 0;
            }}
            header {{
                background: #1a73e8;
                color: white;
                padding: 1.5rem;
                text-align: center;
                font-size: 1.8rem;
            }}
            section {{
                padding: 2rem;
                border-bottom: 1px solid #ddd;
            }}
            h2 {{
                color: #1a73e8;
            }}
            .box {{
                background: white;
                padding: 1.2rem;
                border: 1px solid #ccc;
                border-radius: 8px;
                white-space: pre-wrap;
                line-height: 1.5;
            }}
            footer {{
                background: #eee;
                padding: 1rem;
                text-align: center;
                font-size: 0.85rem;
            }}
        </style>
    </head>
    <body>
        <header>{titulo}</header>

        <section>
            <h2>🧾 Sumário Executivo</h2>
            <div class="box">
Projeto: Data Warehouse Receita Federal (CNPJ)
Data de Execução: {__import__('datetime').datetime.now().strftime('%d/%m/%Y %H:%M')}
Ferramentas utilizadas: CrewAI, Ollama, dbt, Airbyte, PostgreSQL
Output técnico gerado por agentes multi-função com base em input de requisitos da Receita Federal
            </div>
        </section>

        <section>
            <h2>📐 Modelo Lógico de Dados</h2>
            <div class="box">{modelo}</div>
        </section>

        <section>
            <h2>🏗️ Plano de Infraestrutura</h2>
            <div class="box">{infra}</div>
        </section>

        <section>
            <h2>✅ Parecer de Validação Final</h2>
            <div class="box">{parecer}</div>
        </section>

        <footer>
            Projeto gerado automaticamente com CrewAI + LLMs locais (Ollama) · Desenvolvido por você 🧠⚙️
        </footer>
    </body>
    </html>
    """

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"📄 Dashboard final gerado: {path}")
