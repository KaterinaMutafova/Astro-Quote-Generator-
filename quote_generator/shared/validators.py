from django.core.exceptions import ValidationError


def has_email(value):
    if not value:
        raise ValidationError('Трябва да въведете email.')
    return value


def has_quote(value):
    if not value:
        raise ValidationError('Трябва да въведете цитат.')
    return value