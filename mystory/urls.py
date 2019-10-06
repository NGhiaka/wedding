from django.conf.urls import url
 
from . import views
app_name = "mystory"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^co-dau$', views.About_Her, name='about_her'),
    url(r'^chu-re$', views.About_Him, name='about_him'),
    url(r'^nhat-ky/$', views.Stories, name='story'),
    url(r'^thiệp-cuoi/$', views.Invitation, name='invitation'),
    url(r'^khoanh-khac/$', views.Galleries, name='gallery'),
    # url(r'^nhat-ky/$', views.Journal, name='journal'),
    url(r'^loi-chuc/$', views.Blessings, name='blessing'),
]