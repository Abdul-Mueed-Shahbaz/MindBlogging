from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser
)
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import ForeignKey, CASCADE

from apps.common.models import BaseModel


class UserManager(BaseUserManager):
    def create(self, email, username, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        normalized_email = self.normalize_email(email)
        user = self.model(
            email=normalized_email,
            username=username,
        )
        user.set_password(password)  # Set the password
        user.save(using=self._db)
        return user

    def create_staff(self, email, username, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create(
            email,
            username=username,
            password=password
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create(
            email,
            username=username,
            password=password
        )
        user.staff = True
        user.admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    created_on = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # Include 'password' in required fields.

    class Meta:
        db_table = "user"

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.staff

    @property
    def is_admin(self):
        """Is the user an admin member?"""
        return self.admin


class UserRelationship(BaseModel):
    following_user = ForeignKey(User, on_delete=CASCADE, related_name="follower")
    followed_author = ForeignKey(User, on_delete=CASCADE, related_name="author")

    class Meta:
        db_table = "user_relationship"
        unique_together = ('following_user', 'followed_author')

    def clean(self):
        if self.following_user == self.followed_author:
            raise ValidationError("A user cannot follow themselves.")

    def save(self, *args, **kwargs):
        self.clean()
        super(UserRelationship, self).save(*args, **kwargs)
