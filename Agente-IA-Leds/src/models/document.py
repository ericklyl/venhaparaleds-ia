"""
Classe Document para representar documentos PDF.
"""
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Document:
    """
    Representa um documento PDF e seus estados de processamento.
    
    Atributos:
        path (str): Caminho para o arquivo PDF
        name (str): Nome do documento
        raw_text (str, opcional): Texto bruto extraído do PDF
        key_points (List[str], opcional): Pontos-chave extraídos do documento
        summary (str, opcional): Resumo gerado do documento
        blog_post (str, opcional): Post de blog formatado
    """
    path: str
    name: str = ""
    raw_text: Optional[str] = None
    key_points: List[str] = field(default_factory=list)
    summary: Optional[str] = None
    blog_post: Optional[str] = None
    
    def __post_init__(self):
        """Define o nome se não for fornecido."""
        if not self.name:
            self.name = self.path.split("/")[-1]