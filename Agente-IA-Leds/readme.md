# Documentação Completa: PDF to Blog - Desafio LEDS

## Sumário
- [Visão Geral](#visão-geral)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Requisitos e Instalação](#requisitos-e-instalação)
- [Componentes Principais](#componentes-principais)
  - [Agentes](#agentes)
  - [Ferramentas](#ferramentas)
  - [Serviços](#serviços)
- [API REST](#api-rest)
- [Fluxo de Processamento](#fluxo-de-processamento)
- [Testes](#testes)
- [Integração Contínua](#integração-contínua)
- [Análise de Qualidade de Código](#análise-de-qualidade-de-código)


## Visão Geral

O projeto "PDF to Blog" é uma solução baseada em agentes inteligentes para processar documentos PDF, extrair informações relevantes, gerar resumos concisos e transformá-los em posts de blog bem estruturados.

O sistema utiliza o framework CrewAI para orquestrar múltiplos agentes especializados, cada um responsável por uma etapa específica do processo. Além da funcionalidade principal de processamento em lote, o projeto inclui uma API REST que permite interagir com o sistema através de requisições HTTP.

### Objetivos do Projeto

1. Automatizar a leitura e extração de texto de documentos PDF
2. Identificar informações relevantes nos documentos
3. Gerar resumos concisos e informativos
4. Formatar o conteúdo como posts de blog bem estruturados
5. Disponibilizar a funcionalidade através de uma API REST
6. Implementar práticas modernas de desenvolvimento (CI/CD, análise de código)

## Arquitetura do Sistema

O sistema está estruturado em camadas, seguindo princípios de arquitetura modular e Clean Code:

1. **Camada de Apresentação**
   - API REST (FastAPI)
   - Interface de documentação Swagger

2. **Camada de Serviço**
   - Orquestração dos agentes (CrewAI)
   - Processamento de PDFs

3. **Camada de Domínio**
   - Agentes especializados
   - Ferramentas de processamento

4. **Camada de Infraestrutura**
   - Gestão de arquivos
   - Logging
   - Tratamento de exceções

## Tecnologias Utilizadas

- **Linguagem Principal**: Python 3.12+
- **Framework de Agentes**: CrewAI 0.105.0
- **Processamento de PDF**: PyPDF2 3.0.1, pdfplumber 0.11.5
- **Modelos de IA**: Gemini (via crewai-tools 0.37.0)
- **API Web**: FastAPI 0.115.11, Uvicorn 0.34.0
- **Integração com LLMs**: LangChain 0.3.20, OpenAI 1.65.5
- **Testes**: pytest 8.3.5, pytest-cov 6.0.0, coverage 7.6.12
- **Formatação e Linting**: black 24.8.0, isort 5.13.2, flake8 7.0.0
- **CI/CD**: GitHub Actions
- **Análise de Qualidade**: SonarQube
- **Gerenciamento de Dependências**: pip, setuptools
- **Docker**

## Todos os diferenciais foram implementados!

## Estrutura do Projeto

```
desafio-leds-pdf-blog/
├── README.md                   # Documentação geral do projeto
├── requirements.txt            # Dependências do projeto
├── setup.py                    # Configuração para instalação do pacote
├── sonar-project.properties    # Configuração para análise SonarQube
├── .github/                    # Configurações do GitHub
│   └── workflows/
│       ├── ci.yml              # Workflow de CI/CD
│       └── sonarqube.yml       # Workflow para análise SonarQube
├── pdfs/                       # Diretório para PDFs de entrada
├── resultados/                 # Diretório para posts de blog gerados
├── src/
│   ├── __init__.py
│   ├── main.py                 # Ponto de entrada para processamento em lote
│   ├── server.py               # Servidor da API
│   ├── api.py                  # Definição da API REST
│   ├── config.py               # Configurações do projeto
│   ├── exceptions.py           # Classes de exceção personalizadas
│   ├── logging_config.py       # Configuração de logging
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── pdf_reader_agent.py # Agente para leitura de PDFs
│   │   ├── analysis_agent.py   # Agente para análise de informações
│   │   ├── summary_agent.py    # Agente para geração de resumos
│   │   └── format_agent.py     # Agente para formatação de blog posts
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── pdf_tools.py        # Ferramentas para processamento de PDFs
│   │   ├── text_processing_tools.py # Ferramentas para processamento de texto
│   │   └── blog_formatting_tools.py # Ferramentas para formatação de blogs
│   ├── services/
│   │   ├── __init__.py
│   │   └── pdf_blog_service.py # Serviço de processamento de PDFs
│   ├── models/
│   │   ├── __init__.py
│   │   └── document.py         # Modelo de documento
│   └── utils/
│       ├── __init__.py
│       └── helpers.py          # Funções auxiliares
└── tests/
    ├── __init__.py
    ├── test_basic.py           # Testes básicos de importação
    ├── test_agents/
    │   └── test_tools/
    │       └── test_pdf_tools.py # Testes para ferramentas de PDF
```

## Requisitos e Instalação

### Pré-requisitos

- Python 3.10 ou superior
- Chaves de API para serviços de IA (Google/Gemini)
- Git (para clonar o repositório)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/desafio-leds-pdf-blog.git
cd desafio-leds-pdf-blog
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Instale o projeto em modo de desenvolvimento:
```bash
pip install -e .
```

4. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione suas chaves de API:
```
GOOGLE_API_KEY=sua-chave-google-api
GEMINI_API_KEY=sua-chave-gemini-api
OPENAI_API_KEY=FAKE_KEY
```

5. Crie as pastas necessárias (se não existirem):
```bash
mkdir -p pdfs resultados
```

### Executando o Projeto

#### Processamento em Lote (CLI)

Para processar PDFs em lote via linha de comando:

```bash
python -m src.main
```

#### Servidor API

Para iniciar o servidor API:

```bash
python -m src.server
```

Após iniciar o servidor, acesse:
- http://localhost:8000/docs - Para documentação interativa da API
- http://localhost:8000 - Para a API principal

## Componentes Principais

### Agentes

O sistema utiliza quatro agentes especializados do CrewAI:

1. **Agente Leitor de PDF** (`pdf_reader_agent.py`)
   - **Função**: Extrair e validar o texto bruto dos PDFs
   - **Entrada**: Caminho para o arquivo PDF
   - **Saída**: Texto extraído e validado

2. **Agente Analista** (`analysis_agent.py`)
   - **Função**: Analisar o texto e extrair informações importantes
   - **Entrada**: Texto bruto do PDF
   - **Saída**: Pontos-chave e informações organizadas

3. **Agente Resumidor** (`summary_agent.py`)
   - **Função**: Gerar um resumo conciso e coerente
   - **Entrada**: Pontos-chave extraídos
   - **Saída**: Resumo do conteúdo

4. **Agente Formatador** (`format_agent.py`)
   - **Função**: Transformar o resumo em um post de blog formatado
   - **Entrada**: Resumo do conteúdo
   - **Saída**: Post de blog completo com título, subtítulos, introdução e conclusão

### Ferramentas

1. **PDF Tools** (`pdf_tools.py`)
   - `pega_pdfs()`: Encontra todos os arquivos PDF em um diretório
   - Gerencia carregamento e validação de arquivos PDF

2. **Text Processing Tools** (`text_processing_tools.py`)
   - `extrair_texto_pdf()`: Extrai texto de arquivos PDF
   - Implementa lógica para lidar com páginas problemáticas

3. **Blog Formatting Tools** (`blog_formatting_tools.py`)
   - Funções para formatação de elementos do blog
   - Suporte a formatação Markdown

### Serviços

O componente principal de serviço é o `pdf_blog_service.py`:

- **Função**: Orquestrar todo o fluxo de processamento
- **Métodos principais**:
  - `processar_pdfs()`: Gerencia o fluxo de trabalho do início ao fim
  - `save_uploaded_pdf()`: Salva PDFs enviados via API
  - `get_all_pdfs()`: Lista todos os PDFs disponíveis
  - `process_pdf()`: Processa um único PDF
  - `process_multiple_pdfs()`: Processa vários PDFs

## API REST

A API REST é implementada usando FastAPI e oferece endpoints para todas as funcionalidades do sistema.

### Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | / | Retorna informações básicas sobre a API |
| POST | /upload-pdf/ | Faz upload de um arquivo PDF |
| GET | /pdfs/ | Lista todos os PDFs disponíveis |
| POST | /process/{filename} | Processa um PDF específico |
| POST | /process-all/ | Processa todos os PDFs disponíveis |
| GET | /result/{filename} | Obtém um arquivo de resultado específico |
| DELETE | /pdfs/{filename} | Remove um PDF específico |
| DELETE | /results/{filename} | Remove um arquivo de resultado |

### Exemplos de Uso

#### Upload de PDF

```bash
curl -X 'POST' \
  'http://localhost:8000/upload-pdf/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@documento.pdf;type=application/pdf'
```

#### Listar PDFs

```bash
curl -X 'GET' \
  'http://localhost:8000/pdfs/' \
  -H 'accept: application/json'
```

#### Processar um PDF

```bash
curl -X 'POST' \
  'http://localhost:8000/process/documento.pdf' \
  -H 'accept: application/json'
```

#### Obter Resultado

```bash
curl -X 'GET' \
  'http://localhost:8000/result/documento_blog.md' \
  -H 'accept: text/markdown'
```

## Fluxo de Processamento

1. **Recebimento do PDF**
   - Upload via API ou colocação direta na pasta `pdfs/`

2. **Extração de Texto**
   - Leitura do PDF página por página
   - Tratamento de páginas problemáticas
   - Concatenação do texto extraído

3. **Análise e Extração de Informações**
   - Identificação dos pontos-chave do documento
   - Organização das informações por relevância

4. **Geração de Resumo**
   - Criação de um resumo conciso do conteúdo
   - Manutenção da coerência e das informações essenciais

5. **Formatação do Blog**
   - Criação de título chamativo
   - Organização em subtítulos
   - Adição de introdução e conclusão
   - Formatação em Markdown

6. **Armazenamento do Resultado**
   - Salvamento do post formatado na pasta `resultados/`

## Testes

O projeto utiliza pytest para testes automatizados. A estrutura de testes inclui:

1. **Testes Básicos**
   - Verifica importações corretas de módulos

2. **Testes de Ferramentas**
   - Testes para as ferramentas de processamento de PDF
   - Verifica se os PDFs são corretamente encontrados e processados

3. **Cobertura de Código**
   - Relatório de cobertura gerado para análise do SonarQube

### Executando os Testes

```bash
# Executar todos os testes
pytest

# Executar testes com cobertura
pytest --cov=src tests/ --cov-report=xml
```

## Integração Contínua

O projeto utiliza GitHub Actions para automação de CI/CD. Dois workflows principais são configurados:

### CI/CD Pipeline

Arquivo: `.github/workflows/ci.yml`

Este workflow é acionado em pushes e pull requests para branches principais:

1. **Testes**: Executa testes unitários, verifica formatação e gera relatório de cobertura
2. **Build**: Cria um pacote instalável do projeto

### Análise de Qualidade de Código

Arquivo: `.github/workflows/sonarqube.yml`

Este workflow é acionado para analisar a qualidade do código:

1. Executa testes com cobertura
2. Envia os resultados para o SonarQube
3. Utiliza segredos configurados (SONAR_TOKEN, SONAR_HOST_URL) para autenticação

## Análise de Qualidade de Código

O projeto utiliza SonarQube para análise estática de código. A configuração é definida no arquivo `sonar-project.properties`.

### Métricas Atuais

- **Bugs**: 0
- **Vulnerabilidades**: 0
- **Code Smells**: 2
- **Cobertura**: 0,0% de linhas não cobertas (cobertura excelente)
- **Duplicação**: 11,0%
- **Linhas de Código**: 432

### Executando a Análise Localmente

```bash
# Garantir que o SonarQube esteja rodando (Docker ou instalação local)
sonar-scanner -Dsonar.host.url=http://localhost:9000 -Dsonar.login="seu-token"
```

