from fastapi import APIRouter

user_router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@user_router.get('/')
def user():
    pass