from django.db import models
from django.conf import settings
from django.urls import reverse

from .utils import code_generator, create_shortcode
from .validators import validate_url

SHORTCODE_MAX = getattr (settings, 'SHORTCODE_MAX', 15)


#Custom Manager
class DirURLManager(models.Manager):
    ''' Custom Manager for DirURL class '''

    def all(self, *args, **kwargs):
        ''' return only the active links  '''
        queryset = super().all(*args, **kwargs).filter(active = True)
        return queryset
    
    def refresh_codes( self, *args, **kwargs ):
        '''Recreates the shortcodes  '''
        new_codes = 0
        all_objs = super().filter(id__gte = 1)
        for obj in all_objs:
            obj.shortcode = create_shortcode(obj)
            print(obj.shortcode)
            obj.save()
            new_codes += 1
        return print("total new code made :{0}".format(new_codes))

# Models
class DirURL( models.Model ):
    '''  Model class for shortening urls   '''
    url         = models.CharField( max_length = 255 ,  validators = [validate_url])
    shortcode   = models.CharField(max_length = SHORTCODE_MAX , unique = True, blank=True)
    updated     = models.DateTimeField(auto_now = True)
    created     = models.DateTimeField(auto_now_add=True)
    active      = models.BooleanField(default= True)

    objects      = DirURLManager()

    def save( self, *args, **kwargs ):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super().save(*args, **kwargs)

    def __str__( self ):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
    
    def get_short_url(self):
        return "http://tirr.com:8000/{shortcode}".format(shortcode=self.shortcode)   