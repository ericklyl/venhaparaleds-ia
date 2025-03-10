
"""
Ferramentas para formatação de posts de blog.
"""

def formatar_titulo(titulo):
    """formata um título para post de blog"""
    return f"# {titulo}\n\n"

def formatar_subtitulo(subtitulo):
    """formata um subtítulo para post de blog"""
    return f"## {subtitulo}\n\n"

def formatar_paragrafo(texto):
    """formata um parágrafo para post de blog"""
    return f"{texto}\n\n"

def formatar_conclusao(texto):
    """formata a conclusão para post de blog"""
    return f"## Conclusão\n\n{texto}\n"