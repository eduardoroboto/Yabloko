# Manual

O app tem os seguintes tecnologias que precisam ser instaladas.

* Flask
* flask_sqlalchemy
* flask_migrate
* flask_marshmallow
* marshmallow_sqlalchemy

E os pacotes de desenvolvimento, que foram usandas para os testes.

* requests
* ipdb
* coverage
* pytest

## Pipenv

Para instalar todas essas tecnologias sem dificuldades, há um arquivo chamado pipfile, ele é o arquivo que declara todos os pacotes.

Pipenv é um gerenciador e ambientes virtuais python.

Instale ele atráves do seu gerenciador de pacotes ou atraves do pip install

```bash
pip install pipenv
```

Apos instalar abre o terminal nesta pasta onde se encotra esse pdf e execute.


```bash
pipenv install --dev
```

Ele vai automaticamente criar o ambiente virtual desse projeto e instalar todos esses pacotes necessáios tantos o do app quando o de desenvolvimento.

Para entrar no ambiente virtual recem criado de dentro da pasta execute o comando.

```bash
pipenv shell
```

## Como rodar esse projeto

Exporte esses comandos de dentro do ambiente virtual e de flask-run que o projeto vai rodar

```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```

## Como fazer as migrações

Para o app e os testes funcionarem o banco de dados deve ser criado,
rode no terminal de dentro do ambiente.

```sh
flask db init
flask db migrate
flask db upgrade
```
Esse comando vai gerar um arquivo data.db, é o que o projeto utiliza como banco de dados.

## Como rodar os testes e obter cobertura

gera o report e roda os testes utilizando o unittest

```sh
coverage run --source=app -m unittest discover -s test/ -v
```

gera o report e roda os testes utilizando o pytest


```sh
coverage run --source=app -m pytest test/ -v
```


```sh
coverage report
coverage html
```

"coverage report" mostra um resumo da cobertura em shell'

"coverage html"  gera o path '/htmlcov' com htmls estáticos da cobertura
