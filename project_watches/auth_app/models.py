from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_name(value):
    for i in value:
        if not i.isalpha():
            raise ValidationError('Name must contain only alphabet characters!')


class Profile(models.Model):
    MAX_LENGTH_NAME = 20
    gender_choices = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )

    first_name = models.CharField(null=True, blank=True, max_length=MAX_LENGTH_NAME, validators=[validate_name])

    last_name = models.CharField(null=True, blank=True, max_length=MAX_LENGTH_NAME, validators=[validate_name])

    email = models.EmailField(null=True, blank=True, unique=True, )

    image = models.URLField(null=True, blank=True)

    gender = models.CharField(null=True, blank=True,
                              choices=gender_choices,
                              max_length=6)

    age = models.PositiveIntegerField(null=True, blank=True, validators=[validators.MinValueValidator(16)], )

    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class Contact(models.Model):
    MAX_LENGTH_NAME = 20
    MAX_LENGTH_SUBJECT = 50

    email = models.EmailField(null=False, blank=False)

    name = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_NAME)

    subject = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_SUBJECT)

    description = models.TextField(null=False, blank=False)
