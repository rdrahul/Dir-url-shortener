from django.core.validators import URLValidator
from django.core.exceptions  import ValidationError

def validate_url(value):
    ''' validates if given value is url  '''
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError("Invalid Url for this Field")
    return value
