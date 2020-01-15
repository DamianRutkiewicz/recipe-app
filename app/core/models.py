from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                      PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        """ten if mowi ze jesli nie podamy email to zwroci jak
        throw Error z message User must have..."""

        user = self.model(email=self.normalize_email(email), **extra_fields)
        """base user model nie wymaga hasla wiec dodajemy go dopiero pozniej"""
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """custom user model that supports using email instead using username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
