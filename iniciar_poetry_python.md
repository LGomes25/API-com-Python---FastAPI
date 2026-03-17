# Fluxo Sequencial de Configuração de Projeto com Poetry

Guia passo a passo desde a inicialização do projeto até a verificação final do ambiente virtual.

---

## 1. Inicializar o projeto Poetry
```
poetry init
```

**O que acontece**
- Cria o arquivo **pyproject.toml**
- Define informações básicas do projeto
- Estrutura inicial de dependências

**O que observar**
- O arquivo `pyproject.toml` deve aparecer na pasta do projeto
- No formato moderno ele começa com:
> [project] < 

---

## 2. Verificar se o arquivo de configuração é válido
```
poetry check
```

**O que acontece**
- Valida a sintaxe do `pyproject.toml`

**O que observar**
Saída esperada:
> All set!

ou
> pyproject.toml is valid

Se houver erro, ele indicará o campo incorreto.

---

## 3. Criar o ambiente virtual do projeto
```
poetry install
```

**O que acontece**
- Cria o ambiente virtual
- Gera o arquivo `poetry.lock`
- Instala dependências definidas no projeto

**O que observar**
Mensagem semelhante a:
> Creating virtualenv fastapi-blog in ...fastApi_blog.venv

Isso indica que o ambiente está sendo criado **dentro da pasta do projeto**.

---

## 4. Instalar dependências ignorando instalação do pacote do projeto
```
poetry install --no-root
```

**O que acontece**
- Instala apenas dependências
- Não tenta instalar o projeto como pacote Python

**Quando usar**
Projetos de **API ou scripts**, onde o projeto não é distribuído como biblioteca.

**O que observar**
> Installing dependencies from lock file

---

## 5. Executar Python dentro do ambiente Poetry
```
poetry run python
```

**O que acontece**
- Executa Python usando o ambiente virtual criado pelo Poetry

**O que observar**
Dentro do interpretador execute:
```

* import sys
* print(sys.executable)
```

O caminho exibido deve conter:
> .venv\Scripts\python.exe

Isso confirma que o ambiente virtual está sendo utilizado.

---

## 6. Instalar dependências do projeto
```
poetry add fastapi uvicorn
```

**O que acontece**
- Instala bibliotecas no ambiente virtual
- Atualiza `pyproject.toml`
- Atualiza `poetry.lock`

**O que observar**
Instalação de pacotes semelhantes a:

```
Installing fastapi
Installing uvicorn
Installing starlette
Installing pydantic
```

Essas são dependências internas do framework.

---

## 7. Executar comandos do projeto dentro do ambiente

Exemplo:

* poetry run uvicorn main:app --reload

**O que acontece**
- Executa o servidor da aplicação usando o ambiente virtual
- Recarrega automaticamente ao alterar código

**O que observar**
Mensagem semelhante a:
> Uvicorn running on [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 8. Listar ambientes virtuais associados ao projeto
```
poetry env list --full-path
```

**O que acontece**
- Mostra todos os ambientes virtuais vinculados ao projeto

**O que observar**

Exemplo esperado:
> ...\fastApi_blog.venv (Activated)

Isso indica que o ambiente ativo está **dentro da pasta do projeto**.

---

## 9. Verificar informações detalhadas do ambiente
```
poetry env info
```

**O que acontece**
- Exibe detalhes completos do ambiente virtual

**O que observar**
Campos importantes:

```
Virtualenv
Path: ...fastApi_blog.venv
Python: 3.12.x
Executable: ....venv\Scripts\python.exe
Valid: True
```

Esses dados confirmam que:

- o ambiente está ativo
- o Python correto está sendo utilizado
- o ambiente é válido

---

### 10. Configurar o interpretador Python no VS Code

**Objetivo**
Garantir que o **VS Code utilize o Python do ambiente virtual (`.venv`) criado pelo Poetry**, evitando conflitos com o Python global do sistema.

*Abrir o seletor de interpretador*

No VS Code pressione:
> Ctrl + Shift + P

Digite:
> Python: Select Interpreter

*Selecionar o interpretador do projeto*

Caso apareça automaticamente, selecione o interpretador que contém:
> .venv

Exemplo:
> Python 3.12 (.venv)

*Se não aparecer na lista, selecione manualmente:*
> Enter interpreter path

Depois:
> Find...

E navegue até o arquivo:
> fastApi_blog/.venv/Scripts/python.exe

**O que observar**
Após selecionar corretamente, o VS Code mostrará algo semelhante a:
> ...\fastApi_blog.venv\Scripts\python.exe        Workspace

**Significado:**
- `.venv` → ambiente virtual do projeto
- `Workspace` → interpretador configurado apenas para este projeto

*Confirmar que o interpretador está correto*
Abra um novo terminal no VS Code e execute:
```
poetry run python
```

Dentro do Python execute:
```
* import sys
* print(sys.executable)
```

Saída esperada:
> ...\fastApi_blog.venv\Scripts\python.exe

Isso confirma que o **terminal e o VS Code estão usando o ambiente virtual correto**.

---

# Estrutura final esperada do projeto

```
fastApi_blog
│
├── .venv
├── main.py (quando incluso)
├── pyproject.toml
├── poetry.lock
```

---

# Fluxo resumido

```

poetry init
poetry check
poetry install
poetry install --no-root
poetry run python
poetry add fastapi uvicorn
poetry env list --full-path
poetry env info

```

Este fluxo garante:

- ambiente virtual isolado
- dependências controladas
- projeto reproduzível
- configuração correta para desenvolvimento.
```