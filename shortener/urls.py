from django.conf.urls import url
from .views import DirView
urlpatterns = [
    
    url( r'^(?P<shortcode>\w+){6,15}/$' , DirView.as_view(), name = "Home" )
]