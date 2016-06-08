from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/new/$', views.category_new, name='category_new'),
    url(r'^category/(?P<pk>\d+)/edit/$', views.category_edit, name='category_edit'),
    url(r'^category/(?P<pk>\d+)/$', views.category_detail, name='category_detail'),
]