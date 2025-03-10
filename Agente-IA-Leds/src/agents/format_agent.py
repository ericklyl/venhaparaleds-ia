"""
Agente responsável pela formatação do conteúdo em blog.
"""
from crewai import Agent, LLM
from config import GEMINI_API_KEY

# configurar modelo de ia
gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.1,
    api_key=GEMINI_API_KEY
)

# cria agente formatador
agt_formata_docs = Agent(
    role="formatador de conteúdo",
    goal="formatar resumo como um post de blog, incluindo título, subtítulos e conclusão",
    backstory="voce é um agente especialista em transformar conteúdos técnicos em postagens bem estruturadas e atrativas",
    llm=gemini_llm
)