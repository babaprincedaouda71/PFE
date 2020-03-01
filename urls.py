from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url('form', views.register, name = 'form'),
    url('validation', views.valid, name = 'validation'),
    url('about', views.about, name = 'about'),
    url('home', views.home, name = 'home'),
    #url(r'^$', views.new_ind, name = 'new_ind'),
]
