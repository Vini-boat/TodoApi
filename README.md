# TodoApi

Referente ao trabalho de Grau B da disciplina de Engenharia de Software: Arquitetura e Padrões

## Para executar:

Criar e ativar o venv

```shell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar dependências

```shell
pip install -r ./requirements.txt
```

Configurar o `.env` ou usar o `.env.example`

```shell
mv .env.example .env
```

Executar o servidor

```shell
uvicorn app.main:app --reload --port 8080
```
