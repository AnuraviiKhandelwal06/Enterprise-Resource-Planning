from app.repository.users_repository import UserRepository
from app.utils.security import hash_password
from app.utils.security import verify_password
from app.utils.jwt_handler import create_access_token


class AuthService:

    def __init__(self):
        self.user_repository = UserRepository()

    def signup(self, user):
        hashed_password = hash_password(
            user.password
        )
        self.user_repository.create_user(
            username=user.username,
            email=user.email,
            password_hash=hashed_password
        )
        return {
            "message": "User registered successfully"
        }
        
        
    def login(self, user):

        db_user = self.user_repository.get_user_by_email(
        user.email
        )
        if not db_user:
            return {
            "message": "Invalid email or password"
            }
        stored_password_hash = db_user[3]
        if not verify_password(
        user.password,
        stored_password_hash
        ):
            return {
            "message": "Invalid email or password"
            }
        token = create_access_token(
        {
            "sub": db_user[2]
        }
        )
        return {
        "access_token": token,
        "token_type": "bearer"
        }