from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin,admindocs
admin.autodiscover()
from main import views
urlpatterns = [
    # Examples:
    path('', views.home),
    path('shorturl/', include('shorten.urls')),
    path('i18n', include('django.conf.urls.i18n')),

]
