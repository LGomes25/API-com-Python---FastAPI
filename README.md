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
│       ├── database.py           # Configuração da conexão com o banco de dados
│       ├── models/               # Modelos SQLAlchemy para o banco
│       ├── .env.example          # Exemplo de variáveis de ambiente para o banco
├── README.md                     # Documentação principal do repositório
```

---

## ⚙️ Configuração com venv

O projeto utiliza **venv** para gerenciar o ambiente virtual e um arquivo `requirements.txt` para dependências.


### Instalação e configuração inicial

1. Crie o ambiente virtual (dentro da pasta do projeto `fastApi_blog`):
	```
	cd 01-api_assincronas_fastApi/fastApi_blog
	python -m venv .venv
	```

2. Copie o arquivo de exemplo de variáveis de ambiente e configure conforme seu ambiente:
	```
	cp .env.example .env
	# Edite o arquivo .env com usuário, senha, host e nome do banco
	```

3. Crie o banco de dados no PostgreSQL (obrigatório antes de rodar as migrations):
	- Acesse o PostgreSQL (via psql, pgAdmin ou outro cliente) e execute:
	  ```sql
	  CREATE DATABASE fastapi_db;
	  ```

4. Instale as dependências (com o ambiente virtual já ativado, veja instruções abaixo):
	```
	pip install -r requirements.txt
	```

5. Execute as migrations Alembic para criar as tabelas:
	```
	alembic upgrade head
	```

	> **Observação:** O passo anterior (criação do banco) é obrigatório. O Alembic não cria o banco, apenas as tabelas.




---

## 🟢 Ativando, executando e desativando o ambiente virtual

### 1. Ativando o ambiente virtual

O ambiente virtual deve ser ativado dentro da pasta onde ele foi criado (`fastApi_blog`).

No terminal, navegue até a pasta:

```
cd 01-api_assincronas_fastApi/fastApi_blog
```

Ative o ambiente virtual conforme seu sistema operacional:

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

### 2. Executando a API

Após ativar o ambiente virtual, volte para a pasta `01-api_assincronas_fastApi` (um nível acima):

```
cd ..
```

Execute o servidor FastAPI usando o caminho de pacote:

```
uvicorn fastApi_blog.main:app --reload
```

**No navegador:**
```
http://127.0.0.1:8000/
```

**Documentação interativa (Swagger):**
```
http://127.0.0.1:8000/docs
```


**Autenticação JWT obrigatória:**
Todos os endpoints (exceto login) exigem autenticação Bearer JWT.

1. Faça login no endpoint `/auth/login` para obter um token:
	 - Envie um POST para `/auth/login` com o corpo:
		 ```json
		 { "user_id": 1 }
		 ```
	 - O retorno será:
		 ```json
		 { "access_token": "<seu_token_aqui>" }
		 ```

2. Use o token retornado como Bearer Token no header Authorization para acessar os outros endpoints:
	 - Exemplo de header:
		 ```
		 Authorization: Bearer <seu_token_aqui>
		 ```

**Testes com Postman ou HTTP Client:**
- Inclua o token JWT no header Authorization para acessar os endpoints protegidos.

### 3. Desativando o ambiente virtual

Quando terminar de usar, desative o ambiente virtual com:

```
deactivate
```

---
> Dica: Veja também o arquivo `fastApi_blog/INSTRUCOES_EXECUCAO.md` para um passo a passo detalhado.


📖 Observações
- A API agora utiliza Postgres como banco de dados, com SQLAlchemy para ORM.
- O arquivo .env define as credenciais de acesso ao banco.
- O requirements.txt lista todas as dependências, incluindo SQLAlchemy, asyncpg, alembic e psycopg2-binary.
- Não há mais dados mockados em memória; todos os dados são persistidos no banco.
- A pasta controllers concentra a lógica de negócio.
- A pasta models/ contém os modelos SQLAlchemy.
- A pasta views expõe os endpoints FastAPI.
- O ambiente virtual .venv é criado com venv.

---

Este README reflete a estrutura atualizada do projeto e será expandido conforme novos capítulos e exemplos forem adicionados.

---
