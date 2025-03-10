"""
Ferramentas para processamento de texto de PDFs.
"""
import PyPDF2
import os
from PyPDF2 import PdfReader
from src.exceptions import pdfextractionerror

def extrair_texto_pdf(pdf_path):
    """extrai texto de um pdf, ignorando páginas problemáticas"""
    if not os.path.exists(pdf_path):
        print(f"erro: arquivo não encontrado - {pdf_path}")
        return ""

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            texto = ""
            total_paginas = len(reader.pages)
            
            print(f"📄 tentando extrair texto de {total_paginas} páginas do pdf '{os.path.basename(pdf_path)}'...")

            for i in range(total_paginas):
                try:
                    pagina_texto = reader.pages[i].extract_text() or ""
                    texto += pagina_texto + "\n\n"
                    print(f"página {i+1}/{total_paginas} extraída com sucesso.")
                except Exception as e:
                    print(f"erro ao extrair página {i+1}/{total_paginas}: {str(e)}")

            if not texto.strip():
                print(f"erro: nenhuma página extraída com sucesso do pdf '{os.path.basename(pdf_path)}'.")
                return ""

            print(f"✅ extração concluída! total de caracteres extraídos: {len(texto)}")
            return texto

    except Exception as e:
        print(f"erro crítico ao abrir o pdf: {str(e)}")
        return ""