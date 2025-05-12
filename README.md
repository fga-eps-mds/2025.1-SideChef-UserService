# 2025.1-SideChef-UserService

## Como rodar o projeto

### Criar ambiente virtual
```
python3 -m venv .venv
```

### Ativar ambiente
### For linux or mac
```
source .venv/bin/activate
```

### For windows
```
venv\Scripts\activate
```

### Instalar as dependências
```
pip install -r requirements.txt
```

### .env

Subistituir valores em $.

```
cp .env.local .env

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

### Opcional Rodar as migrações inicias para criar um usuário
```
alembic upgrade head
```

### Rodar o código
```
fastapi dev main.py
```

### Comandos Adicionais

1-Adicionar uma nova migração
'''
alembic revision --autogenerate -m "mensagem"
'''