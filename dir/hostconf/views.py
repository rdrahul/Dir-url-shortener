from django.http import HttpResponseRedirect
from django.conf import settings

DEFAULT_REDIRECT_URL  = getattr(settings, "DEFAULT_REDIRECT_URL","http://www.tirr.com:8000") 

def wildcard_redirect(request, path =None):
    ''' Redirect to main domain from any subdomain  '''
    if path is not None:
        new_url = DEFAULT_REDIRECT_URL + "/" + path
    return HttpResponseRedirect(new_url)