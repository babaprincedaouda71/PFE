from django.conf.urls import url
from . import views

app_name='pages'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'form/$', views.register, name = 'form'),
    url(r'validation/$', views.valid, name = 'validation'),
    url(r'about/$', views.about, name = 'about'),
    url(r'personalPage/$', views.personalPageView, name = 'personalPage'),
    url(r'home/$', views.home, name = 'home'),
    url(r'login/$', views.login_view,name="login"),
    url(r'login/$', views.login_view,name="login"),
    url(r'logout/$', views.logout_view,name="logout"),
    url(r'signup/$', views.signup_view, name="signup"),
    url(r'diplome/$', views.register1, name="diplome"),
    url(r'test/$', views.testView, name="test"),
    url(r'diplomeCandidat/$', views.diplomeCandidatView1, name="diplomeCandidat"),
    url(r'inscription/$', views.registerFormView, name="inscription"),
]
