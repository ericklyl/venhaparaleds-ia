"""
Configurações da aplicação.
"""
import os
from pathlib import Path

# configuração do diretorio
BASE_DIR = Path(__file__).parent.parent
PDF_DIR = os.path.join(BASE_DIR, "pdfs")
RESULTS_DIR = os.path.join(BASE_DIR, "resultados")

# garante que os diretórios existem
os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# Configuração da API de LLM
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Configuração de logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "app.log")