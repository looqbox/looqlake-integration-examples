# Looqbox Integration Examples

## Sobre
Este repositório tem como objetivo compartilhar com nossos clientes exemplos de integrações automatizadas com as soluções de Big Data da Looqbox.

Para facilitar, os exemplos foram divididos em pastas, que contem todos detalhes necessários para executar o exemplo.

As informações detalhadas de configuração de cliente, como por exemplo os locais e as credenciais para acesso, serão encaminhadas pela área de projeto da Looqbox diretamente aos reponsáveis pelo projeto do lado do cliente.

Está página servirá de sumário para descrever quais são os exemplos disponíveis até o momento. Vale lembrar que a medida que avançarmos na evolução do produto, termos novos exemplos disponíveis dentro deste repositório.

Os exemplos disponívels foram criados na linguagem.

- Python

## Instruções

- Em cada uma das pastas no arquivo README.md contem os detalhes de como executar o exemplo.


## Estrutura dos exemplos
| Pasta        | Descritivo |
---------------|------------
| buckets      | Contem exemplos de como enviar as informações para seu bucket aqui dentro da looqbox|

## Download do repositório

- Defina um diretório de trabalho onde será baixado o repositório, por exemplo:

```bash
mkdir ~/looqbox
```

- Entre no diretório
```bash
cd ~/looqbox
```

- Baixe o repositório local

```bash 
 git clone git@github.com:looqbox/looqlake-integration-examples.git
```

## Credenciais
A credencial é um arquivo no formato json que será enviado para o cliente. 

**Vale ressaltar que cada cliente possui a sua credencial e será de sua responsabilidade (cliente) em gerenciar o permissionamento dentro de seu ambiente.**

Para que funcione nos exemplos, a credencial devera ser gravada no arquivo:

 ```
 ~/looqbox/looqlake-integration-examples/LOOQBOX_CREDENTIALS.json
 ```

 - Crie a seguinte variável de ambiente: ```GOOGLE_APPLICATION_CREDENTIALS``` com o valor para o caminho absoluto desta arquivo.

 ```bash
 export GOOGLE_APPLICATION_CREDENTIALS=~/looqbox/looqlake-integration-examples/LOOQBOX_CREDENTIALS.json
 ```


# Pontos importantes
- Estes códigos disponíbilizados, servem apenas como exemplo e funcionam no escopo de integração, por isso não devem ser usados diretamente em produção.

- A responsabilidade de implementação de processos automatizados ficam a cargo do cliente.
