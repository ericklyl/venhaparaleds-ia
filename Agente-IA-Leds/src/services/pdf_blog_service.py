from crewai import Crew
from src.exceptions import agentprocessingerror
from src.logging_config import log
from src.tools.text_processing_tools import extrair_texto_pdf
from src.agents import agt_ler_pdf, agt_extrai_pdf, agt_gera_resumo, agt_formata_docs
from crewai import Task

def processar_pdfs(lista_pdfs):
    """processa múltiplos pdfs e lida com erros no crewai."""
    try:
        log("iniciando processamento dos pdfs...")
        
        for pdf in lista_pdfs:
            nome_pdf = pdf.split("/")[-1]
            log(f"processando pdf: {nome_pdf}")
            
            # extrai o texto antes de rodar os agentes
            texto_extraido = extrair_texto_pdf(pdf)
            
            if not texto_extraido.strip():
                log(f"⚠️ erro: o texto do pdf {nome_pdf} está vazio ou não pôde ser extraído.", "error")
                continue  # pula para o próximo pdf
            
            # recriando tarefas para incluir o texto extraído
            trf_ler_pdf = Task(
                description=f"""
                o texto extraído do pdf '{nome_pdf}' é:
                
                {texto_extraido[:1000]}... [cortado para visualização]
                
                confirme se o texto foi extraído corretamente e passe para o próximo agente.
                """,
                expected_output="texto extraído do pdf",
                agent=agt_ler_pdf
            )

            trf_extrai_pdf = Task(
                description="""
                analise e extraia informações mais importantes do texto que foi extraído pelo agente anterior.
                identifique os pontos mais importantes, dados relevantes e informações principais.
                organize os pontos por tópicos, eliminando informações redundantes.
                """,
                expected_output="lista de entendimentos e pontos importantes extraídos do documento",
                agent=agt_extrai_pdf
            )

            trf_resume_pdf = Task(
                description="""
                gere um resumo do conteúdo analisado pelo agente anterior.
                crie um texto conciso que capture as informações essenciais.
                evite repetições e mantenha a coerência do texto.
                """,
                expected_output="resumo conciso e bem estruturado do documento",
                agent=agt_gera_resumo
            )

            trf_formata = Task(
                description="""
                formate o resumo criado pelo agente anterior em estilo e forma de um post de blog.
                inclua:
                - um título chamativo que desperte interesse
                - subtítulos organizados que estruturem o conteúdo
                - uma introdução envolvente
                - desenvolvimento lógico das ideias principais
                - uma conclusão bem elaborada
                - formatação adequada para leitura na web
                """,
                expected_output="post de blog bem estruturado com título, subtítulos e conclusão",
                agent=agt_formata_docs
            )

            time = Crew(
                agents=[agt_ler_pdf, agt_extrai_pdf, agt_gera_resumo, agt_formata_docs],
                tasks=[trf_ler_pdf, trf_extrai_pdf, trf_resume_pdf, trf_formata],
                verbose=True
            )

            log("crewai configurado com sucesso. iniciando agentes...")

            try:
                postagem = time.kickoff()
                log(f"✅ resumo do pdf {nome_pdf} gerado com sucesso!")
                return postagem
            except Exception as e:
                log(f"⚠️ erro ao processar {nome_pdf}: {str(e)}", "error")

    except agentprocessingerror as e:
        log(str(e), "error")

    except Exception as e:
        log(f"erro inesperado no processamento: {str(e)}", "error")