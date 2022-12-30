from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


USERNAME_VALIDATOR = RegexValidator(
    regex = r'^[a-zA-Z0-9_.-]+$',
    message = 'Username must be alphanumeric, with no spaces.'
)

EMAIL_ADDRESS_VALIDATOR = RegexValidator(
    regex = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])",
    message = 'Email address does not have a correct format.'
)


class User(AbstractUser):
    ''' Modified User model from django.contrib.auth.models.User '''

    firstname = models.CharField(
        max_length = 30,
        null = False,
        verbose_name = 'First Name'
    )

    lastname = models.CharField(
        max_length = 30,
        null = False,
        verbose_name = 'Last Name'
    )

    username = models.CharField(
        max_length = 30,
        validators = [USERNAME_VALIDATOR],
        null = False,
        unique = True,
        verbose_name = 'Username'
    )

    email = models.EmailField(
        max_length = 254,
        validators = [EMAIL_ADDRESS_VALIDATOR],
        unique = True,
        verbose_name = 'Email Address'
    )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.email