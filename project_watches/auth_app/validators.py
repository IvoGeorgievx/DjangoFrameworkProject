from django.core.exceptions import ValidationError


def validate_name(value):
    for i in value:
        if not i.isalpha():
            raise ValidationError('Name must contain only alphabet characters!')