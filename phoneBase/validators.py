from django.core.exceptions import ValidationError


def details_validate(value):
    if value is None or value == '':
        raise ValidationError('to pole nie moze byc puste')
    else:
        return value


def general_validate(value):
    if value is None or '':
        raise ValidationError('to pole nie moze byc puste')
    else:
        return value
