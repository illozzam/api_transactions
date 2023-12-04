# Teste Objective

## Instruções para instalação

O projeto foi desenvolvido utilizando Docker e docker-compose, com a API em Django, Django Rest Framework e banco de dados em MySQL.

Optei por desenvolver todo o código, os endpoints e os campos do banco de dados em inglês, mantendo em português apenas a documentação e retornos de erros.

Dessa forma, os endpoints são:

```
GET /account/?account_id=1234

POST /account/
    input => JSON {"account_id": 1234, "balance": 500}

POST /transaction/
    input => JSON {"account": 1234, "operation": "P", "amount": 10}
```

Para executar o projeto, certifique-se primeiro de ter um arquivo *.env* no mesmo diretório do *docker-compose.yaml* contendo as seguintes variáveis:
```
MYSQL_DATABASE -> Nome do banco de dados
MYSQL_ROOT_PASSWORD -> Senha do usuário root do banco de dados.

DEBUG -> True para modo debug do Django e False para produção.
SECRET_KEY -> Valor da SECRET_KEY do projeto Django.
```

Após isso, estando no mesmo diretório do arquivo *docker-compose.yaml*, execute o comando:
```docker-compose up -d```

Após o comando, aguarde um tempo até que o banco de dados inicialize e a aplicação tenha condições de sincronizar com o banco. **O projeto deve rodar no endereço 172.16.0.3.**

Deixei também um comando no arquivo *Dockerfile* comentado para a execução dos testes unitários. Para isso, descomente as linhas 14 e 15 e comente as linhas posteriores, mantendo somente um CMD em execução.