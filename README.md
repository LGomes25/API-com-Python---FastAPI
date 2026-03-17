# API com Python - FastAPI

Este repositório reúne estudos e práticas sobre **FastAPI**, framework moderno e de alto desempenho para construção de APIs em Python.  
O conteúdo está organizado em capítulos e exemplos práticos, cobrindo desde conceitos introdutórios até tópicos avançados como manipulação de banco de dados, autenticação, testes e deploy.

---

## 🎯 Objetivo
- Explorar os fundamentos de APIs RESTful  
- Aprender a criar endpoints assíncronos com FastAPI  
- Integrar banco de dados relacionais  
- Implementar autenticação e autorização  
- Realizar testes automatizados  
- Preparar e realizar deploy de aplicações  

---

## 📂 Estrutura do Projeto

A organização atual do repositório segue uma estrutura modular, com diretórios dedicados a diferentes capítulos e exemplos.  
O projeto principal em andamento está dentro da pasta `01-api_assincronas_fastApi/fastApi_blog`.
```
API COM PYTHON - FASTAPI
├── .vscode/                      # Configurações específicas do VS Code
├── 01-api_assincronas_fastApi/   # Capítulo focado em APIs assíncronas
│   └── fastApi_blog/             # Projeto principal FastAPI
│       ├── .venv/                # Ambiente virtual isolado criado pelo Poetry
│       ├── controllers/          # Camada de controle (regras de negócio e rotas)
│       │   └── post.py
│       ├── models/               # Modelos de dados
│       │   └── schemas/          # Schemas Pydantic para validação
│       │       └── post.py
│       ├── services/             # Serviços auxiliares (ex: lógica externa, utilitários)
│       ├── views/                # Endpoints FastAPI (camada de apresentação)
│       │   ├── main.py           # Ponto de entrada da aplicação FastAPI
│       │   └── post.py
│       ├── pyproject.toml        # Configuração do Poetry e dependências
│       ├── poetry.lock           # Lockfile de dependências (versões exatas)
│       ├── about_poetry.md       # Documentação sobre uso do Poetry
│       └── iniciar_poetry_python.md # Guia inicial de configuração do Poetry
├── README.md                     # Documentação principal do repositório
```

---

## ⚙️ Configuração com Poetry

O projeto utiliza **Poetry** para gerenciar dependências e ambientes virtuais.  
Principais arquivos:
- `pyproject.toml` → define nome do projeto, versão, autores e dependências.  
- `poetry.lock` → garante reprodutibilidade das versões instaladas.  
- `.venv/` → ambiente virtual isolado criado pelo Poetry.  

Dependências principais:
- **FastAPI** → framework para criação de APIs assíncronas.  
- **Uvicorn** → servidor ASGI para rodar a aplicação.  

---

## ▶️ Executando a API

**No terminal (dentro da pasta do projeto):**
```
poetry run uvicorn views.main:app --reload
```

**No navegador:**
```
http://127.0.0.1:8000/
```

**Documentação interativa (Swagger):**
```
http://127.0.0.1:8000/docs
```

**Testes com Postman ou HTTP Client:**
- Criar requisições para os endpoints definidos em controllers/ e views/

---

📖 Observações
- A pasta controllers concentra a lógica de negócio.
- A pasta models/schemas define os modelos de dados (ex: Pydantic).
- A pasta views expõe os endpoints FastAPI.
- O ambiente virtual .venv é criado automaticamente pelo Poetry dentro do projeto.
- Arquivos auxiliares (about_poetry.md, iniciar_poetry_python.md) documentam o uso do Poetry e boas práticas.

---

Este README reflete a estrutura atualizada do projeto e será expandido conforme novos capítulos e exemplos forem adicionados.

---
