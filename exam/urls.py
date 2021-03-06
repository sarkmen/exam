from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^shopping/', include('shopping.urls', namespace='shopping')),
    url(r'^$', lambda request: redirect('/shopping/')),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)