from sqlalchemy import text
from app.database.connection_db import SessionLocal


class UserRepository:
    def create_user(self, username, email, password_hash):
        session = SessionLocal()
        try:
            query = text("""
                INSERT INTO users
                (username, email, password_hash)
                VALUES
                (:username, :email, :password_hash)
            """)
            session.execute(
                query,
                {
                    "username": username,
                    "email": email,
                    "password_hash": password_hash
                }
            )
            session.commit()
        finally:
            session.close()
            
    def get_user_by_email(self, email):
        session = SessionLocal()
        try:
            query = text("""
            SELECT *
            FROM users
            WHERE email = :email
            """)
            result = session.execute(
            query,
            {"email": email}
            )
            return result.fetchone()
        finally:
            session.close()        