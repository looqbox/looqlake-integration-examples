# Looqbox Big Data Solution - Buckets

## Sobre
Nesta pasta contem os exemplo de como criar uma integração automatizada para enviar arquivos para os Buckets do Cliente que são disponibilizados pela Looqbox.

## Ponto importante - Pastas dentro do Bucket


|pasta             | Descritivo          |
|------------------|---------------------|
|encaminhados      | fluxo de produção   |
|processados       | arquivos que já foram consumidos pelo fluxo automatizado|
|nao-mapeados      | arquivos que não existem mapeamentos correlacionados|
|test-robot        | usado para testes automatizados do lado do cliente, esses arquivos não serão consumidos e serão excluidos após 24 horas| 

### Testes de integração
Para testes de integração, dentro do bucket foi criado uma pasta ```test-robot``` que serve exclusivamente para fazer testes de integração.

Os arquivos que estão dentro desta ```test-robot``` não serão processados, servem apenas para que o cliente possa fazer os testes automatizados, sem afetar o fluxo de produção.

Porém no fluxo de produção os arquivos deverão ser salvos na pasta ```encaminhados``` dessa forma o mecanismo automatizado da looqbox de ingestão dos dados será executado.

### Python
Os exemplos foram criados na linguagem ```python```, os detalhes de instalação e como executar encontram-se disponíveis em [README-Python](python-example/README-python.md)

