import os
import pytest
from src.tools.pdf_tools import pega_pdfs
from src.exceptions import pdfnotfounderror

def test_pega_pdfs_empty_directory(tmp_path):
    """testa se a função gera a exceção correta quando o diretório está vazio"""
    with pytest.raises(pdfnotfounderror):
        pega_pdfs(str(tmp_path))

def test_pega_pdfs_with_pdfs(tmp_path):
    """testa se a função retorna os PDFs corretamente"""
    # cria alguns arquivos PDF falsos
    pdf1 = tmp_path / "test1.pdf"
    pdf2 = tmp_path / "test2.pdf"
    pdf1.write_text("fake pdf")
    pdf2.write_text("fake pdf")
    
    result = pega_pdfs(str(tmp_path))
    assert len(result) == 2
    assert str(pdf1) in result or str(pdf2) in result