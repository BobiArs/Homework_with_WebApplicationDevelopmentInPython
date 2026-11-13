import os
import uuid
from django.contrib.auth.hashers import make_password
from .models import User

class UserService:
    @staticmethod
    def register_user(first_name: str, last_name: str, email: str, password: str, birth_date=None, avatar=None) -> User:
        if User.objects.filter(email=email).exists():
            raise ValueError("Користувач із таким email уже існує.")

        # Генеруємо унікальне ім'я файлу для аватара (щоб уникнути перезапису однакових назв)
        if avatar:
            ext = os.path.splitext(avatar.name)[1]
            avatar.name = f"{uuid.uuid4()}{ext}"

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password_hash=make_password(password),
            birth_date=birth_date if birth_date else None,
            avatar=avatar,
            is_active=True
        )
        user.save()
        return user