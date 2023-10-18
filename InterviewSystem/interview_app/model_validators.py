import re
from django.core.exceptions import ValidationError


def name_validator(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('The name cannot contain digits.')
    return value


def phone_number_validator(value):
    pattern = r'(\+\d{9,15}$)'
    the_match = re.match(pattern, value)
    if not the_match:
        raise ValidationError("Value must start with '+' followed by 9 up to 15 digits.")
    return value