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
│       ├── .venv/                # Ambiente virtual isolado criado com venv
│       ├── controllers/          # Camada de controle (regras de negócio e rotas)
│       │   └── post.py
│       ├── models/               # Modelos de dados
│       │   └── schemas/          # Schemas Pydantic para validação
│       │       └── post.py
│       ├── services/             # Serviços auxiliares (ex: lógica externa, utilitários)
│       ├── views/                # Endpoints FastAPI (camada de apresentação)
│       │   ├── main.py           # Ponto de entrada da aplicação FastAPI
│       │   └── post.py
│       ├── requirements.txt      # Dependências do projeto para instalação via pip
├── README.md                     # Documentação principal do repositório
```

---

## ⚙️ Configuração com venv

O projeto utiliza **venv** para gerenciar o ambiente virtual e um arquivo `requirements.txt` para dependências.

### Passos para configurar o ambiente:

1. Crie o ambiente virtual (dentro da pasta do projeto):
	```
	python -m venv .venv
	```
2. Ative o ambiente virtual:
	 - **Windows (PowerShell):**
		 ```
		 . .venv\Scripts\Activate.ps1
		 ```
	 - **Windows (Prompt de Comando):**
		 ```
		 .venv\Scripts\activate.bat
		 ```
	 - **Linux/macOS:**
		 ```
		 source .venv/bin/activate
		 ```

#### Problemas comuns no Windows

Se aparecer erro de permissão ao ativar o venv no PowerShell:

1. Execute este comando no PowerShell (apenas uma vez):
	 ```
	 Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
	 ```
2. Feche e abra um novo terminal PowerShell e tente ativar novamente.

Se continuar com erro, tente ativar pelo Prompt de Comando (cmd.exe):
```
.venv\Scripts\activate.bat
```
3. Instale as dependências:
	```
	pip install -r requirements.txt
	```

### Executando a API

No terminal (com o ambiente ativado, dentro da pasta do projeto):
```
uvicorn main:app --reload
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
- O ambiente virtual .venv é criado com venv.
- O arquivo requirements.txt lista as dependências do projeto.

---

Este README reflete a estrutura atualizada do projeto e será expandido conforme novos capítulos e exemplos forem adicionados.

---
