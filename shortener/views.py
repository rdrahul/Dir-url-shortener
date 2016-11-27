from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse , HttpResponseRedirect

from .models import DirURL
from .forms import SubmitUrlForm
from analytics.models import UrlAnalysis

class DirView(View):
    def get(self, request, shortcode=None):
        obj = get_object_or_404( DirURL , shortcode = shortcode)
        print( UrlAnalysis.objects.create_analysis(obj) )
        return HttpResponseRedirect(obj.url )


class HomeView(View):
    def get(self, request , *args, **kwargs):
        form = SubmitUrlForm()
        print ("here")
        return render(request , "shortener/home.html" , {"form": form } )
    
    def post(self, request , *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {'form' : form}
        template = 'home.html'
        
        if form.is_valid():
            data = form.cleaned_data
            print (data)
            obj , created = DirURL.objects.get_or_create( **data )
            url_count = UrlAnalysis.objects.filter(dir_url = obj).first() or 0
            if url_count != 0:
                print (url_count)
                url_count = url_count.count
            else:
                url_count = 0
            print (url_count)
            template = 'success.html'
            context = { 'object' : obj,
                        'count' : url_count
                    }

        return render(request , "shortener/"+template, context)