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

Executar o servidor

```shell
uvicorn app.main:app --reload --port 8080
```
