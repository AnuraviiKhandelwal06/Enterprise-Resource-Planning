from app.services.auth_services import AuthService

class AuthController:

    def __init__(self):
        self.auth_service = AuthService()

    def signup_controller(self, user):
        return self.auth_service.signup(user)

    def login_controller(self, user):
        return self.auth_service.login(user)