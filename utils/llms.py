from langchain_community.chat_models import ChatLiteLLM

def get_llms():
    return {
        "analista": ChatLiteLLM(model="ollama/deepseek-r1:latest", config={"timeout": 1200}),
        "modelador": ChatLiteLLM(model="ollama/deepseek-r1:latest", config={"timeout": 1200}),
        "infra": ChatLiteLLM(model="ollama/codellama:python", config={"timeout": 1200}),
        "pipelines": ChatLiteLLM(model="ollama/codellama:python", config={"timeout": 1200}),
        "validador": ChatLiteLLM(model="ollama/deepseek-r1:latest", config={"timeout": 1200}),
        "gerente": ChatLiteLLM(model="ollama/deepseek-r1:latest", config={"timeout": 1200}),
    }
