from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models


class UserManager(BaseUserManager):
    def create(self, email, first_name, last_name):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        normalized_email = self.normalize_email(email)
        user = self.model(
            email=normalized_email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_staff(self, email, first_name, last_name):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create(
            email,
            first_name=first_name,
            last_name=last_name
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create(
            email,
            first_name=first_name,
            last_name=last_name
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    password = None
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Email & Password are required by default.

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.staff

    @property
    def is_admin(self):
        """Is the user a admin member?"""
        return self.admin
