from django.db import models

from shortener.models import DirURL

class UrlAnalysisManager(models.Manager):
    ''' Manager class for UrlAnalysis model '''
    def create_analysis(self,instance):
        ''' counts the no. of times the link has been accessed '''
        if isinstance(  instance, DirURL ):
            obj, created = self.get_or_create( dir_url = instance )
            obj.count += 1
            obj.save()
            return obj.count
        return None

class UrlAnalysis(models.Model):
    dir_url  = models.OneToOneField( DirURL )
    count   = models.IntegerField( default =0 )
    ip_addr = models.CharField( max_length=25, blank=True, null=True )
    updated = models.DateTimeField( auto_now = True )
    created = models.DateTimeField( auto_now_add = True )
    objects = UrlAnalysisManager()