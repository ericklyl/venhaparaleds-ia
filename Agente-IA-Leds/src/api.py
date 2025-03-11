import src.helper 
import os
import shutil
from pathlib import Path
from typing import List

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
# Para execução local
# from services.pdf_blog_service import processar_pdfs

# Para execução no Docker
from src.services.pdf_blog_service import processar_pdfs
from src.tools.pdf_tools import pega_pdfs
from src.exceptions import pdfnotfounderror
from src.logging_config import log
from src.utils.helpers import salvar_resultado
from fastapi.responses import HTMLResponse



app = FastAPI(
    title="PDF to Blog API",
    description="API para processamento de PDFs e geração de posts de blog",
    version="1.0.0",
)

# configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# diretórios pra armazenamento
BASE_DIR = Path(__file__).parent.parent
PDF_DIR = BASE_DIR / "pdfs"
RESULTS_DIR = BASE_DIR / "resultados"

# garante que os diretorios existem
os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# monta diretorio estatico pra acessar os resultados
app.mount("/resultados", StaticFiles(directory=str(RESULTS_DIR)), name="resultados")


@app.get("/")
def read_root():
    """Endpoint raiz da API."""
    return {"message": "API de Processamento de PDFs para Blogs. Use /docs para documentação."}


@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Faz upload de um arquivo PDF
    
    Args:
        file: Arquivo PDF para upload
    
    Returns:
        dict: Informações sobre o arquivo carregado
    """
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Apenas arquivos PDF são permitidos")
    
    file_path = PDF_DIR / file.filename
    
    try:
        # Salva o arquivo
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        log(f"PDF '{file.filename}' enviado com sucesso")
        
        return {
            "filename": file.filename,
            "status": "uploaded",
            "message": "Arquivo PDF enviado com sucesso"
        }
    
    except Exception as e:
        log(f"Erro ao salvar o arquivo: {str(e)}", "error")
        raise HTTPException(status_code=500, detail=f"Erro ao processar o upload: {str(e)}")


@app.get("/pdfs/")
def list_pdfs():
    """Lista todos os PDFs disponíveis para processamento"""
    try:
        pdfs = pega_pdfs(str(PDF_DIR))
        return {"pdfs": [Path(pdf).name for pdf in pdfs]}
    except pdfnotfounderror:
        return {"pdfs": []}
    except Exception as e:
        log(f"Erro ao listar PDFs: {str(e)}", "error")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/process/{filename}")
def process_pdf(filename: str):
    """
    Processa um PDF específico
    
    Args:
        filename: Nome do arquivo PDF a ser processado
    
    Returns:
        dict: Resultado do processamento
    """
    pdf_path = PDF_DIR / filename
    
    if not pdf_path.exists():
        raise HTTPException(status_code=404, detail=f"PDF não encontrado: {filename}")
    
    try:
        # Processar o PDF
        post_content = processar_pdfs([str(pdf_path)])
        
        # Salvar o resultado
        result_filename = f"{filename.split('.')[0]}_blog.md"
        result_path = salvar_resultado(str(post_content), result_filename)
        
        # URL para acessar o arquivo
        result_url = f"/resultados/{result_filename}"
        
        return {
            "filename": filename,
            "status": "processed",
            "result_file": result_filename,
            "result_url": result_url
        }
    
    except Exception as e:
        log(f"Erro ao processar {filename}: {str(e)}", "error")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/process-all/")
def process_all_pdfs():
    """Processa todos os PDFs disponíveis"""
    try:
        pdfs = pega_pdfs(str(PDF_DIR))
        results = []
        
        for pdf in pdfs:
            try:
                pdf_name = Path(pdf).name
                post_content = processar_pdfs([pdf])
                
                # Salvar o resultado
                result_filename = f"{pdf_name.split('.')[0]}_blog.md"
                result_path = salvar_resultado(str(post_content), result_filename)
                
                # URL para acessar o arquivo
                result_url = f"/resultados/{result_filename}"
                
                results.append({
                    "filename": pdf_name,
                    "status": "processed",
                    "result_file": result_filename,
                    "result_url": result_url
                })
                
            except Exception as e:
                results.append({
                    "filename": Path(pdf).name,
                    "status": "error",
                    "error": str(e)
                })
        
        return {"results": results}
    
    except pdfnotfounderror:
        raise HTTPException(status_code=404, detail="Nenhum PDF encontrado para processamento")
    except Exception as e:
        log(f"Erro ao processar PDFs: {str(e)}", "error")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/result/{filename}")
def get_result_file(filename: str):
    """
    Recupera um arquivo de resultado específico
    
    Args:
        filename: Nome do arquivo de resultado
    
    Returns:
        FileResponse: Arquivo de resultado
    """
    file_path = RESULTS_DIR / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail=f"Arquivo não encontrado: {filename}")
    
    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="text/markdown"
    )

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "templates")), name="static")

@app.get("/ui", response_class=HTMLResponse)
async def get_ui():
    """Interface web para uso da API."""
    with open(BASE_DIR / "templates" / "index.html", "r") as file:
        return file.read()

@app.delete("/pdfs/{filename}")
def delete_pdf(filename: str):
    """Remove um PDF específico."""
    file_path = PDF_DIR / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail=f"PDF não encontrado: {filename}")
    
    try:
        os.remove(file_path)
        return {"message": f"PDF {filename} removido com sucesso"}
    except Exception as e:
        log(f"erro ao remover PDF: {str(e)}", "error")
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/results/{filename}")
def delete_result(filename: str):
    """remove um arquivo de resultado específico."""
    file_path = RESULTS_DIR / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail=f"Arquivo não encontrado: {filename}")
    
    try:
        os.remove(file_path)
        return {"message": f"Arquivo {filename} removido com sucesso"}
    except Exception as e:
        log(f"Erro ao remover arquivo: {str(e)}", "error")
        raise HTTPException(status_code=500, detail=str(e))