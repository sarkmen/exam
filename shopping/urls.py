from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/new/$', views.category_new, name='category_new'),
    url(r'^category/(?P<pk>\d+)/edit/$', views.category_edit, name='category_edit'),
    url(r'^category/(?P<pk>\d+)/$', views.category_detail, name='category_detail'),
    url(r'^category/(?P<pk>\d+)/delete/$', views.category_delete, name='category_delete'),
    url(r'^category/(?P<category_pk>\d+)/shop/new/$', views.shop_new, name='shop_new'),
    url(r'^category/(?P<category_pk>\d+)/shop/(?P<pk>\d+)/edit/$', views.shop_edit, name='shop_edit'),
    url(r'^category/(?P<category_pk>\d+)/shop/(?P<pk>\d+)/$', views.shop_detail, name='shop_detail'),
    url(r'^category/(?P<category_pk>\d+)/shop/(?P<pk>\d+)/delete/$', views.shop_delete, name='shop_delete'),
    url(r'^category/(?P<category_pk>\d+)/shop/(?P<shop_pk>\d+)/review/new/$', views.review_new, name='review_new'),
    url(r'^category/(?P<category_pk>\d+)/shop/(?P<shop_pk>\d+)/review/(?P<pk>\d+)/edit/$', views.review_edit, name='review_edit'),
    url(r'^category/(?P<category_pk>\d+)/shop/(?P<shop_pk>\d+)/review/(?P<pk>\d+)/delete/$', views.review_delete, name='review_delete'),

]