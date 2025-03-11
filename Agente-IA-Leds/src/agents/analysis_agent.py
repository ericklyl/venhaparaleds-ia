"""
Agente responsável pela análise e extração de informações
"""
from crewai import Agent, LLM
from src.config import GEMINI_API_KEY

# configurar modelo de ia
gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.1,
    api_key=GEMINI_API_KEY
)

# cria agente analista
agt_extrai_pdf = Agent(
    role="analista de informações",
    goal="identificar informações mais importantes do documento",
    backstory="voce é um agente especialista em analisar e extrair dados importantes de documentos",
    llm=gemini_llm
)