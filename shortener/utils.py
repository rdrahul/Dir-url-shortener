from django.conf import settings

import random 
import string

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)

def code_generator(size = SHORTCODE_MIN , chars = string.ascii_lowercase + string.digits):
    """  Generates the shortcode randomly """
    shortcode = ''.join( random.choice(chars) for _ in range(size)  )
    return shortcode

def create_shortcode(instance, size = SHORTCODE_MIN):
    new_code = code_generator(size = size)
    dirClass = instance.__class__
    query    = dirClass.objects.filter(shortcode = new_code).exists()
    if query:
        return create_shortcode(instance,size=size)
    return new_code
    