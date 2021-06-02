from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class CustomUserManager(BaseUserManager):
    def create_user(self, username, address, email, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(
            username=username, address=address, email=email, **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, address, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        return self.create_user(username, address, email, password, **other_fields)


class my_user(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20)
    address = models.TextField(blank=False)
    email = models.EmailField(unique=True)
    password = models.CharField(blank=False, max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "address", "password"]

    def __str__(self):
        return self.username