import os
import re

def salvar_multiplos_arquivos(conteudo: str, pasta_base="outputs"):
    print("🛠️ Separando arquivos do output do engenheiro de pipelines...")

    padrao = r"---FILENAME---\s*(.*?)\n(.*?)(?=(---FILENAME---|$))"
    matches = re.findall(padrao, conteudo, re.DOTALL)

    if not matches:
        print("⚠️ Nenhum arquivo encontrado no formato esperado.")
        return

    for path, body, _ in matches:
        caminho_completo = os.path.join(pasta_base, path.strip())
        os.makedirs(os.path.dirname(caminho_completo), exist_ok=True)
        with open(caminho_completo, "w", encoding="utf-8") as f:
            f.write(body.strip())
        print(f"✅ Arquivo salvo: {caminho_completo}")
