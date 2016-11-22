from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse , HttpResponseRedirect

from .models import DirURL

class DirView(View):

    model = DirURL
    
    def get(self, request, shortcode):
        print ("elese")
        obj = get_object_or_404(DirURL , shortcode = shortcode)
        return HttpResponseRedirect(obj.url )
