from jose import jwt, JWTError

from app.config.setting import settings
from app.utils.jwt_handler import ALGORITHM


def verify_token(token: str):
    try:
        print("Received Token:", token)
        print("Secret Key:", settings.SECRET_KEY)
        print("Algorithm:", ALGORITHM)

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        print("Decoded Payload:", payload)

        return payload

    except JWTError as e:
        print("JWT Error:", str(e))
        return None