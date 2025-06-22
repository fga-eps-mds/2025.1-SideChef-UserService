from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Hash de Senha
def generate_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(entered_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(entered_password, hashed_password)