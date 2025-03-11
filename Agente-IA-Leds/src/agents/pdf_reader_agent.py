"""
Agente responsável pela leitura de PDFs.
"""
from crewai import Agent, LLM
from src.config import GEMINI_API_KEY

# configura modelo de ia
gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.1,
    api_key=GEMINI_API_KEY
)

# cria agente leitor de PDF
agt_ler_pdf = Agent(
    role="leitor de pdf",
    goal="extrair o texto bruto do pdf",
    backstory="voce é um agente especializado em leitura e extração de pdf",
    llm=gemini_llm
)