from django.urls import path
from django.conf.urls import url
from shorten import views
urlpatterns = [
    path('', views.list), # one empty string indicates the root
    path('new/', views.new,name='new'),
    url(r'^(?P<code>\w{4})/?$', views.redirect_to_url,name='redirect_to_url'), #(?P<code>\w{4}) capture 4 alphanumeric characters.
]