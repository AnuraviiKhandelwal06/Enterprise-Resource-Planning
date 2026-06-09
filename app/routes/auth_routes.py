from fastapi import APIRouter

from app.controllers.auth_controller import AuthController
from app.schemas.user_schema import UserSignup
from app.schemas.user_schema import UserLogin

router = APIRouter()

controller = AuthController()


@router.post("/signup")
def signup(user: UserSignup):
    return controller.signup_controller(user)


@router.post("/login")
def login(user: UserLogin):
    return controller.login_controller(user)