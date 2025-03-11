"""
Pacote de agentes para o processamento de documentos PDF
"""

from src.agents.pdf_reader_agent import agt_ler_pdf
from src.agents.analysis_agent import agt_extrai_pdf
from src.agents.summary_agent import agt_gera_resumo
from src.agents.format_agent import agt_formata_docs

__all__ = [
    "agt_ler_pdf",
    "agt_extrai_pdf",
    "agt_gera_resumo",
    "agt_formata_docs"
]