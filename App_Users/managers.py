from django.contrib.auth.models import UserManager
from django.core.exceptions import ValidationError


class MyUserManager(UserManager):
    def create_user(
        self, email, first_name="", last_name="", password=None, **extra_fields
    ):
        if not email:
            raise ValidationError("Foydalanuvchi uchun email talab qilinadi.")
        email = self.normalize_email(email)
        user = self.model(
            email=email, first_name=first_name, last_name=last_name, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, first_name, last_name, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser uchun `is_staff=True` bo'lishi kerak.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser uchun `is_superuser=True` bo'lishi kerak.")

        return self.create_user(email, first_name, last_name, password, **extra_fields)
