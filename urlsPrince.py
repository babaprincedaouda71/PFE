from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from . import views as user_views

app_name='pages'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'form/$', views.register, name = 'form'),
    url(r'validation/$', views.valid, name = 'validation'),
    url(r'about/$', views.about, name = 'about'),
    url(r'test/$', views.personalPageView, name = 'test'),
    url(r'home/$', views.home, name = 'home'),
    #url(r'login/$', views.loginView,name="login"),

    ### URL to redirect to a profile page
    url(r'profile/$', user_views.profile, name = 'profile'),

    ### Login and logout URL
    url(r'login/$', auth_views.LoginView.as_view(template_name='general/login.html'),name="login"),
    url(r'logout/$', auth_views.LogoutView.as_view(template_name='general/logout.html'),name="logout"),

    ### URL to connect to admintemp
    url(r'loginAsAdmin/$', views.loginAsAdminView,name="loginAsAdmin"),

    ### URL to create a account
    url(r'createAccount/$', views.createAccountView,name="createAccount"),
    #url(r'login/$', views.login_view,name="login"),
    #url(r'logout/$', views.logout_view,name="logout"),
    url(r'signup/$', views.signup_view, name="signup"),
    url(r'diplome/$', views.register1, name="diplome"),
    url(r'test/$', views.testView, name="test"),
    url(r'diplomeCandidat/$', views.diplomeCandidatView1, name="diplomeCandidat"),
    url(r'register/$', views.registerFormView, name="register"),
    url('admintemp', views.admintemp, name = 'admintemp'),
    url('preSelection', views.preSelectionView, name = 'preSelection'),
]


"""
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url('form', views.register, name = 'form'),
    url('validation', views.valid, name = 'validation'),
    url('about', views.about, name = 'about'),
    url('home', views.home, name = 'home'),
    url('admintemp', views.admintemp, name = 'admintemp'),
    url('h3', views.h3, name = 'h3'),
    url('h5', views.h5, name = 'h5'),
    url('home0', views.home0, name = 'home0'),

    #url(r'^$', views.new_ind, name = 'new_ind'),
]
"""
