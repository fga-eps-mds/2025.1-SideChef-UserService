from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha_digitada: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha_digitada, senha_hash)