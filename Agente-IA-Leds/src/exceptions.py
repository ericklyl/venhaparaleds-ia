class pdfnotfounderror(Exception):
    """erro quando um diretório de pdfs não contém arquivos válidos."""
    def __init__(self, path):
        super().__init__(f"nenhum arquivo pdf encontrado no diretório: {path}")

class pdfextractionerror(Exception):
    """erro ao extrair texto de um pdf."""
    def __init__(self, pdf_name, message="falha ao extrair texto do pdf."):
        super().__init__(f"erro no arquivo {pdf_name}: {message}")

class agentprocessingerror(Exception):
    """erro durante o processamento por um agente crewai."""
    def __init__(self, agent_name, message="erro ao processar tarefa do agente."):
        super().__init__(f"{agent_name}: {message}")