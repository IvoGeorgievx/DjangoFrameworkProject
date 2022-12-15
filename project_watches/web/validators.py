from django.core.exceptions import ValidationError


def model_years_validator(value):
    if 1990 > value or value > 2022:
        raise ValidationError('Model must be between years 1990 and 2022(inclusive).')


def belt_price_validator(value):
    if value > 150:
        raise ValidationError('Belt price can not be higher than 150$.')