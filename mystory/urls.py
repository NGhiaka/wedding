from django.conf.urls import url
 
from . import views
app_name = "mystory"
urlpatterns = [
    url(r'^$', views.index, name='index'),
]