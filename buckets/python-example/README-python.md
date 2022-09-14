# Looqbox Big Data Solution

## Sobre
Este exemplo tem como principal objetivo demonstrar como fazer o upload de arquivos de forma automatizada para o mecanismo de buckets do Looqbox usando scripts em Python.


***Os exemplos foram criados com base em Linux e MacOs***

### Pré-Requisitos

- Python 3.10+
- Virtual Env

***Caso não tenha o virutalenv, basta seguir o seguinte tutorial***
https://docs.python.org/3/library/venv.html

Entrar no diretório
```bash
cd looqlake-integration-examples/buckets
```


```bash
virtualenv -p python3.10 python-example
```

Entrar no diretório
```bash
cd python-example
```


### Ativando o virutalenv
```bash
source bin/activate
```

### Atualizando o pip
```bash
bin/python3 -m pip install --upgrade pip
```


### Rodando o requirements
```bash
bin/pip3 install -r requirements.txt
```

## Exportar a variável de ambiente

Essa é uma etapa importante que irá colocar a variável de ambiente onde está o arquivo de credentials da service account.

[Configurando as Credenciais de acesso](../../README.md#credenciais)

## Executando o programa

```bash
python3 upload_bucket.py <nome do bucket> <caminho absoluto do arquivo>
```








