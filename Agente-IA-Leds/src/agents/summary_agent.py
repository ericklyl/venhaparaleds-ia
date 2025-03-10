"""
Agente responsável pela geração de resumos.
"""
from crewai import Agent, LLM
from config import GEMINI_API_KEY

# configura modelo de ia
gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.1,
    api_key=GEMINI_API_KEY
)

# cria agente gerador de resumo
agt_gera_resumo = Agent(
    role="gerador de resumo",
    goal="gerar resumos curtos e coerentes a partir das informações extraídas",
    backstory="voce é um agente especialista em gerar resumos concisos e informativos",
    llm=gemini_llm
)