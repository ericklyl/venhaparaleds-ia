"""
Funções auxiliares para a aplicação.
"""
import os
from src.config import RESULTS_DIR

def validar_caminho(caminho):
    """
    Valida se um caminho existe.
    
    Args:
        caminho (str): Caminho para validar
        
    Returns:
        bool: True se o caminho existir, False caso contrário
    """
    return os.path.exists(caminho)

def salvar_resultado(conteudo, nome_arquivo):
    """
    Salva o conteúdo em um arquivo.
    
    Args:
        conteudo: Conteúdo a ser salvo (string ou CrewOutput)
        nome_arquivo (str): Nome do arquivo onde salvar
        
    Returns:
        str: Caminho completo onde o arquivo foi salvo
    """
    # Usa o diretório de resultados configurado
    diretorio = RESULTS_DIR
    
    # Cria o caminho completo
    caminho_completo = os.path.join(diretorio, nome_arquivo)
    
    # Converte para string se não for
    conteudo_str = str(conteudo)
    
    # Salva o conteúdo
    with open(caminho_completo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo_str)
        
    return caminho_completo