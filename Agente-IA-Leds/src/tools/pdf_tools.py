"""
Ferramentas para processamento de PDFs.
"""
import os
from src.exceptions import pdfnotfounderror
from src.logging_config import log
from src.tools.text_processing_tools import extrair_texto_pdf

def pega_pdfs(local):
    """pega todos os arquivos pdf do diretório"""
    if not os.path.exists(local):
        log(f"diretório não encontrado: {local}", "error")
        return []
    
    pdfs = [os.path.join(local, arquivo) for arquivo in os.listdir(local) if arquivo.lower().endswith('.pdf')]
    
    if not pdfs:
        raise pdfnotfounderror(local)

    log(f"{len(pdfs)} arquivos pdf encontrados.")
    return pdfs