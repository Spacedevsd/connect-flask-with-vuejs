## Baixando e Configurando o Ambiente

Para usar o projeto você deve realizar o clone do mesmo, utilizando o comando abaixo:

```bash
$ git clone git@github.com:spadevs/connect-flask-with-vuejs.git
```

Depois você pode criar uma virtualenv utilizando o Python.

```bash
$ python -m venv .venv
```

Ative a virtualenv:

on Linux:

```bash
$ source .venv/bin/activate
```

on Windows:

```bash
$ .venv/Scripts/Activate.ps1
```

## Instalando Dependências

Como a virtualenv ativada, instale as dependências usando o comando a seguinte:

```bash
$ pip install -r requirements.txt
```

## Criando variáveis de ambientes:

On Linux:
```bash
$ export FLASK_APP=app.app:create_app
```
On Windows:
```bash
$ set FLASK_APP=app.app:create_app
```

## Rodando o projeto:

```bash
$ flask run
```
