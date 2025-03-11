import os
from pathlib import Path
from src.tools.pdf_tools import pega_pdfs
from src.services.pdf_blog_service import processar_pdfs
from src.exceptions import pdfnotfounderror
from src.logging_config import log
from src.utils.helpers import salvar_resultado
from src.config import PDF_DIR

ROOT_DIR = Path(__file__).parent.parent
# diretório onde os pdfs estão
local_pdfs = os.path.join(ROOT_DIR, "pdfs")

os.makedirs(local_pdfs, exist_ok=True)

if __name__ == "__main__":
    try:
        log(f"Procurando PDFs em: {local_pdfs}")
        lista_pdfs = pega_pdfs(local_pdfs)
        
        if not lista_pdfs:
            log("Nenhum PDF encontrado. Encerrando o programa.", "error")
        else:
            log(f"Encontrados {len(lista_pdfs)} PDFs para processamento.")
            for pdf in lista_pdfs:
                log(f"Processando: {os.path.basename(pdf)}")
                postagem = processar_pdfs([pdf])  # Processa um PDF por vez
                
                if postagem:
                    # Extrair o conteúdo da resposta do CrewOutput como string
                    conteudo_str = str(postagem)
                    
                    # Nome do arquivo baseado no nome do PDF
                    nome_arquivo = os.path.basename(pdf).replace('.pdf', '_blog.md')
                    
                    # Salvar o resultado
                    caminho_salvo = salvar_resultado(conteudo_str, nome_arquivo)
                    log(f"Blog post salvo em: {caminho_salvo}")

    except pdfnotfounderror as e:
        log(str(e), "error")
    except Exception as e:
        log(f"Erro inesperado: {str(e)}", "error")