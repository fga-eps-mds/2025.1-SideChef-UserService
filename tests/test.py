from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from main import app
from user.models.user import Base
from user.services.user import create_user, get_all_users
from user.schemas.user import UserCreate


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"APP": "Running"}

client = TestClient(app)

# In-Memory Test Database Setup
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in the in-memory database
Base.metadata.create_all(bind=engine)

# Database fixture for dependency injection in tests
@pytest.fixture
def db():
    db = TestingSessionLocal()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    try:
        yield db
    finally:
        db.close()

# Unit Tests for User Service
def test_create_user(db):
    user_data = UserCreate(
        name="Pedro Amaral",
        email="pedro@example.com",
        password="123456",
        cpf="12345678900"
    )
    user = create_user(db, user_data)

    assert user.id is not None
    assert user.name == "Pedro Amaral"
    assert user.email == "pedro@example.com"
    assert user.cpf == "12345678900"

def test_get_all_users(db):
    # Should start with an empty user list
    users = get_all_users(db)
    assert users == []

    # Create a new user
    user_data = UserCreate(
        name="Maria",
        email="maria@example.com",
        password="senha123",
        cpf="11122233344"
    )
    create_user(db, user_data)

    # Check that the user was added
    users = get_all_users(db)
    assert len(users) == 1
    assert users[0].email == "maria@example.com"
