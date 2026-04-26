# Como rodar o projeto FastAPI corretamente

## Instruções rápidas

1. Abra o terminal na pasta do projeto:
   ```
   cd C:\Treinamento_JS\Python\API_com_Python-FastAPI\01-api_assincronas_fastApi
   ```
2. Ative o ambiente virtual (se ainda não estiver ativo):
   - PowerShell:
     ```
     .venv\Scripts\Activate.ps1
     ```
   - CMD:
     ```
     .venv\Scripts\activate.bat
     ```
3. Instale as dependências (se necessário):
   ```
   pip install -r fastApi_blog/requirements.txt
   ```
4. Copie e edite o arquivo de variáveis de ambiente:
   ```
   copy fastApi_blog\.env.example fastApi_blog\.env
   # Edite fastApi_blog\.env com os dados do seu banco
   ```
5. Crie o banco de dados no PostgreSQL (se ainda não existir):
   ```sql
   CREATE DATABASE fastapi_db;
   ```
6. Execute as migrations Alembic:
   ```
   alembic upgrade head
   ```
7. Rode o servidor FastAPI SEMPRE a partir da pasta 01-api_assincronas_fastApi:
   ```
   uvicorn fastApi_blog.main:app --reload
   ```

- Acesse a documentação em: http://127.0.0.1:8000/docs

## Observações importantes
- NÃO execute `uvicorn main:app --reload` dentro da pasta fastApi_blog. Isso causará erro de importação.
- Sempre rode o comando uvicorn a partir da pasta 01-api_assincronas_fastApi, usando o caminho do pacote: `fastApi_blog.main:app`.
- Se mudar a estrutura de pastas, ajuste o comando conforme necessário.
- Se aparecer erro de importação, revise o diretório atual e o comando usado.
