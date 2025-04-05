import os

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>{titulo}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 2rem;
            background-color: #f5f5f5;
            color: #333;
        }}
        h1 {{
            color: #1a73e8;
        }}
        .section {{
            margin-bottom: 2rem;
        }}
        .box {{
            background: #fff;
            border: 1px solid #ddd;
            padding: 1rem;
            border-radius: 6px;
            white-space: pre-wrap;
        }}
    </style>
</head>
<body>
    <h1>{titulo}</h1>
    <div class="section">
        <div class="box">{conteudo}</div>
    </div>
</body>
</html>
"""

def salvar_html(titulo: str, conteudo: str, path: str):
    html = HTML_TEMPLATE.format(titulo=titulo, conteudo=conteudo)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
