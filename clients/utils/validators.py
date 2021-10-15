from datetime import datetime
from django.conf import settings
from rest_framework.exceptions import ValidationError


def validation_max_results(start, max_results):
    if max_results < start or max_results < 1 or start < 0:
        raise ValidationError('Parameter limit_per_query needs to greater than parameter start.')
    return start, max_results


def validation_boolean(value, parameter_name):
    if value is None:
        return
    if value == 'true':
        return True
    if value == 'false':
        return False

    raise ValidationError(f'Parameter {parameter_name} needs to receive a boolean value.')


def validation_format_date(date, parameter):
    error_message = f'Parameter {parameter} needs to receive a datetime value. Ex: 2021-12-12T22:25:55'

    if date is None:
        return

    try:
        formated_date = date.replace('T', ' ')
        datetime.strptime(formated_date, '%Y-%m-%d %H:%M:%S')
        return date
    except Exception as e:
        raise ValidationError(error_message)


def validation_sex_choice(value):
    if value is None:
        return

    if value in 'FfMm':
        return value
    raise ValidationError('Sex needs receive a "F" or "M')


def validation_age_group(group):
    if group is None:
        return
    
    if group in settings.AGE_GROUP:
        return group
    raise ValidationError(f'Parameter age not have a {group} result.')
