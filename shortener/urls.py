from django.conf.urls import url
from .views import DirView, HomeView
urlpatterns = [
    url(r'^$', HomeView.as_view(), name = "Home" ),
    url( r'^(?P<shortcode>\w+)/$' , DirView.as_view(), name = "Redirect" )
]