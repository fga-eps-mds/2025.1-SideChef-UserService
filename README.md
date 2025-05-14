# 2025.1-SideChef-UserService
## Descrição 
Este repositório visa armazenar o microsserviço UserService do aplicativo SideChef, responsável pela gestão dos usuários do sistema

## Tecnologias
|||
|-----------|--------|
| __Linguagem__ | Python |
| __Backend__ | FastAPI |
| __Banco de Dados__| PostgreSQL |

## Como rodar o projeto

### 1. Instalar o Docker Engine

Primeiramente instale o [Docker](https://www.docker.com) no seu computador.
### 2. Clone o repositório
Clone este repositório na sua máquina.

### 3. Crie o arquivo .env
Dentro do reposítório, crie um arquivo chamado `.env` e adicione as informações enviadas pelos mantenedores, ou configure a própria pelo template:

```
POSTGRESQL_USERNAME=$USERNAME_DB$
POSTGRESQL_PASSWORD=$PASSWORD_DB$
POSTGRESQL_SERVER=$SERVER$
POSTGRESQL_PORT=$PORT_DB$
POSTGRESQL_DATABASE=$DB_NAME$
DOMAIN=$DOMAIN$
ENVIRONMENT=$local$
BACKEND_CORS_ORIGINS=$http://localhost:PORT$
JWT_SECRET_KEY=$JWT$
```
### 4. Execute o docker-compose up

Na pasta do repositório execute o comando:

```
docker-compose up
```

### 5. Acesse a API
Para acessar a API, utilize o *localhost* na porta *8000*:

http://localhost:8000

