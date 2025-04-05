from crewai import Task

def analise_requisitos(agent):
    return Task(
        description="Leia o arquivo 'requisitos.md' na pasta 'inputs' e extraia os principais requisitos do projeto.",
        expected_output="Resumo dos requisitos principais: fontes, KPIs, domínios.",
        agent=agent,
        tools=agent.tools
    )
