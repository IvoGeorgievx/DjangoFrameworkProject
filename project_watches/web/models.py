from django.db import models
from project_watches.auth_app.models import Profile
from project_watches.web.validators import model_years_validator, belt_price_validator

MAX_LENGTH_NAME = 25
MAX_LENGTH_COLOR = 15
MAX_LENGTH_SIZE = 20
MAX_LENGTH_CHOICES = 10


class Watches(models.Model):
    class Meta:
        verbose_name_plural = 'Watches'

    name = models.CharField(max_length=MAX_LENGTH_NAME)

    year = models.PositiveIntegerField(null=False, blank=False, validators=[model_years_validator])

    description = models.TextField(null=False, blank=False)

    image = models.ImageField(null=True, blank=True, upload_to='static/images/')

    price = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class Sunglasses(models.Model):
    class Meta:
        verbose_name_plural = 'Sunglasses'

    choices = (
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    )
    name = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_NAME)

    image = models.ImageField(null=False, blank=False, upload_to='static/images/')

    model_year = models.PositiveIntegerField(null=False, blank=False, validators=[model_years_validator])

    lens_size = models.CharField(null=False, blank=False, choices=choices, max_length=MAX_LENGTH_SIZE)

    lens_color = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_COLOR)

    frame_type = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_SIZE)

    price = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class Wallets(models.Model):
    class Meta:
        verbose_name_plural = 'Wallets'

    choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    name = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_NAME)

    size = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_SIZE)

    image = models.ImageField(null=False, blank=False, upload_to='static/images/')

    ID_window = models.CharField(null=False, blank=False, choices=choices, max_length=MAX_LENGTH_CHOICES)

    coin_pouch = models.CharField(null=False, blank=False, choices=choices, max_length=MAX_LENGTH_CHOICES)

    card_capacity = models.PositiveIntegerField(null=False, blank=False)

    price = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class Belts(models.Model):
    class Meta:
        verbose_name_plural = 'Belts'

    choices = (
        ('Leather', 'Leather'),
        ('Plastic', 'Plastic'),
        ('Heavy Cloth', 'Heavy Cloth'),
    )

    brand = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_NAME)

    image = models.ImageField(null=True, blank=True, upload_to='static/images/', )

    color = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_COLOR)

    material = models.CharField(null=False, blank=False, choices=choices, max_length=MAX_LENGTH_NAME)

    buckle_form = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_NAME)

    price = models.PositiveIntegerField(null=False, blank=False, validators=[belt_price_validator])

    def __str__(self):
        return f'{self.brand}'


class Ties(models.Model):
    class Meta:
        verbose_name_plural = 'Ties'

    choices = (
        ('Polyester', 'Polyester'),
        ('Wool', 'Wool'),
    )

    brand = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_NAME)

    image = models.ImageField(null=False, blank=False, upload_to='static/images/')

    material = models.CharField(null=False, blank=False, choices=choices, max_length=MAX_LENGTH_NAME)

    color = models.CharField(null=False, blank=False, max_length=MAX_LENGTH_COLOR)

    price = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.brand}'
