from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.db import models

USERNAME_REGEX = "^[a-zA-Z0-9.+-]*$"

class Permission(models.Model):
    name = models.CharField(max_length=255)


class Role(models.Model):
    name = models.CharField(max_length=255)
    permission = models.ManyToManyField(Permission)

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("user must have an Email address")
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, verbose_name="email address")

    # password = models.CharField(max_length=255)
    username = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=USERNAME_REGEX,
                message="Username must be alphanumeric or contains numbers",
                code="Invalid Username",
            )
        ],
        unique=True,
    )
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email
