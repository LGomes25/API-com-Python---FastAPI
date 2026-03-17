````markdown
# Guia Prático de Poetry (Python)

O **Poetry** é uma ferramenta moderna para **gerenciar dependências, ambientes virtuais e empacotamento de projetos Python**. Ele substitui combinações tradicionais como `pip + requirements.txt + virtualenv`, oferecendo um fluxo mais organizado e reproduzível.

---

# 1. O que é o Poetry

O Poetry é um **gerenciador de dependências e build system** para Python que:

- cria e gerencia **ambientes virtuais automaticamente**
- controla dependências de forma determinística
- gera **arquivos de lock** para garantir reprodutibilidade
- simplifica publicação de pacotes Python

Arquivos principais do Poetry:

| Arquivo | Função |
|---|---|
| `pyproject.toml` | configuração do projeto e dependências |
| `poetry.lock` | trava versões exatas das dependências |

---

# 2. Instalação do Poetry

## Windows (PowerShell)

no terminal (powershell)
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
ou
```
pip install poetry
```

Verificar instalação:

```
poetry --version
```

---

# 3. Criando um projeto com Poetry

Crie um novo projeto:

```
poetry new meu_projeto
```

Estrutura criada:

```
meu_projeto
│
├── pyproject.toml
├── README.md
├── meu_projeto
│   └── __init__.py
└── tests
```

Entrar no projeto:

```
cd meu_projeto
```

---

# 4. Inicializando Poetry em projeto existente

Se o projeto já existe:

```
poetry init
```

O Poetry fará perguntas sobre:

* nome do projeto
* versão
* dependências
* versão do Python

Isso gera o arquivo `pyproject.toml`.

---

# 5. Gerenciando dependências

## Adicionar dependência

```
poetry add requests
```

O Poetry:

1. instala a biblioteca
2. atualiza `pyproject.toml`
3. atualiza `poetry.lock`

---

## Adicionar dependência de desenvolvimento

```
poetry add pytest --group dev
poetry add 'fastapi=*'
```

Dependências de desenvolvimento incluem:

* testes
* linters
* ferramentas de build

---

## Remover dependência

```
poetry remove requests
```

---

# 6. Instalando dependências do projeto

Quando clonar um projeto com Poetry:

```
poetry install
```

Isso:

* cria o ambiente virtual
* instala tudo conforme `poetry.lock`

---

# 7. Ambiente virtual automático

O Poetry cria ambientes virtuais automaticamente.

Local comum:

```
~/.cache/pypoetry/virtualenvs
```

Ou dentro do projeto (se configurado).

---

# 8. Ativando o ambiente virtual

Entrar no ambiente do projeto:

```
poetry env activate
```

Depois disso:

```
(meu_projeto-py3.11) $
```

Agora todos comandos Python usam o ambiente do projeto.

---

# 9. Executar comandos sem ativar ambiente

Também é possível executar comandos diretamente:

```
poetry run python main.py
```

ou

```
poetry run pytest
```

Isso usa o ambiente virtual automaticamente.

---

# 10. Identificando o ambiente virtual

Ver qual ambiente está sendo usado:

```
poetry env info
```

Exemplo de saída:

```
Virtualenv
Python: 3.11
Path: /home/user/.cache/pypoetry/virtualenvs/projeto-abc123
```

---

# 11. Listar ambientes disponíveis

```
poetry env list
```

Exemplo:

```
projeto-abc123-py3.11 (Activated)
```

---

# 12. Remover ambiente virtual

```
poetry env remove python
```

Ou:

```
poetry env remove 3.11
```

---

# 13. Atualizar dependências

Atualizar dependências respeitando regras do projeto:

```
poetry update
```

---

# 14. Estrutura típica de projeto com Poetry

```
projeto
│
├── pyproject.toml
├── poetry.lock
├── README.md
│
├── src
│   └── app
│       └── main.py
│
└── tests
```

---

# 15. Configuração útil (ambiente dentro do projeto)

Para criar `.venv` dentro da pasta do projeto:

```
poetry config virtualenvs.in-project true
```

Estrutura:

```
projeto
│
├── .venv
├── pyproject.toml
└── poetry.lock
```

Isso facilita integração com:

* VS Code
* Docker
* Dev Containers

---

# 16. Arquivo pyproject.toml (exemplo)

```toml
[tool.poetry]
name = "meu_projeto"
version = "0.1.0"
description = ""
authors = ["Seu Nome"]

[tool.poetry.dependencies]
python = "^3.11"
requests = "^2.31"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4"
```

---

# 17. Fluxo típico de desenvolvimento

Existem dois cenários comuns: criar um projeto novo ou inicializar o Poetry em um projeto já existente.

## 1. Criar um novo projeto
```
poetry new projeto
cd projeto
```
Adicionar dependências:
```
poetry add "fastapi=*"
poetry add "uvicorn[standard]"
```
Ativar o ambiente virtual:
```
poetry env activate
```
Verificar ambientes disponíveis
```
poetry env list
```
Executar Python dentro do ambiente:
```
poetry run python
```
## 2. Inicializar Poetry em projeto existente

Dentro da pasta do projeto:
```
poetry init
```
Adicionar dependências:
```
poetry add "fastapi=*"
poetry add "uvicorn[standard]"
```
Ativar o ambiente virtual:
```
poetry env activate
```
Verificar ambientes disponíveis
```
poetry env list
```
Executar Python dentro do ambiente:
```
poetry run python
```
*Dica: sempre confirme que o Python usado está vindo do ambiente virtual do Poetry.
Use poetry run ou verifique o caminho com poetry env info*

---

# 18. Vantagens do Poetry

* gerenciamento moderno de dependências
* ambientes virtuais automáticos
* lockfile confiável
* integração com ferramentas modernas
* facilita publicação de bibliotecas

---

# 19. Comparação com abordagem tradicional

| Método      | Ferramentas                         |
| ----------- | ----------------------------------- |
| Tradicional | pip + requirements.txt + virtualenv |
| Moderno     | Poetry                              |

Com Poetry:

* menos arquivos
* dependências rastreadas automaticamente
* ambientes gerenciados de forma transparente

---

# Conclusão

O Poetry simplifica o desenvolvimento Python ao **centralizar dependências, ambientes e build do projeto** em uma única ferramenta, tornando projetos mais reproduzíveis e fáceis de manter.

```
```
