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
```
cp .env.local .env
```

### Opcional Rodar as migrações inicias para criar um usuário
```
alembic upgrade head
```

### Rodar o código
```
fastapi dev main.py
```