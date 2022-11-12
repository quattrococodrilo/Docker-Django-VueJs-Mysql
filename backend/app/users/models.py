from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User model
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'User already has taken this email.',
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
