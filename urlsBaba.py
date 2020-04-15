from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from . import views as user_views


### Pour le test de l'edition du formulaire
##from . views import IndividuListView, IndividuDetailView
app_name='pages'
urlpatterns = [

### Page d'accueil
    url(r'^$', views.home, name = 'home'),
    url(r'test/$', views.personalPageView, name = 'test'),


    ### URL to redirect to a profile page
    url(r'profile/$', user_views.profile, name = 'profile'),

    ### URL pout tester l'edition d'un formulaire
    #url(r'test1/$', IndividuListView.as_view(), name="test1"),
    #url(r'test1/<char:pk>/$', IndividuDetailView.as_view(), name="test1_detail"),

    ### Login and logout URL
    url(r'login/$', auth_views.LoginView.as_view(template_name='general/login.html'),name="login"),
    url(r'logout/$', auth_views.LogoutView.as_view(template_name='general/logout.html'),name="logout"),

    ### URL to create an account
    url(r'createAccount/$', views.createAccountView,name="createAccount"),

    ### URL to desactivate an account
    url(r'desactivateAccount/$', views.desactivateAccountView,name="desactivateAccount"),

## preSelection
    url(r'selectCand/$', views.selectCandidatView,name="selectCand"),

## Pour afficher la liste de preselection
    url(r'preSelection/$', views.preSelectionView,name="preSelection"),

## Selection finale
    url(r'selectFinal/$', views.selectFinalView,name="selectFinal"),

## Pour afficher la liste de selection finale
    url(r'selection/$', views.selectionView,name="selection"),

## Pour editer editer les infos de these et Equipe_recherche
    url(r'addInfoDoc/$', views.addInfoDocView,name="addInfoDoc"),

## Pour afficher l'information de utilisateur connecté différents du profile
    url(r'mesInfo/$', views.mesInfoView,name="mesInfo"),


## La page admin des utilisateur
    url(r'personalPage/$', views.personalPageView,name="personalPage"),

### Inscription
#Candidat
    url(r'register/$', views.registerFormView, name="register"),
#Professeur
    url(r'registerProf/$', views.registerProfFormView, name="registerProf"),

    url('admintemp', views.admintemp, name = 'admintemp'),


    #url('candidat_list', views.preSelectionView, name = 'candidat_list'),
    #url('candidatList', views.selectionView, name = 'candidatList'),

### Pour renseigner la date des soutenance
    url('soutDate', views.soutDateView, name = 'soutDate'),


### Pour renseigner la mention du doctorant
    url('mentionDoc', views.mentionDocView, name = 'mentionDoc'),



### creattion de compte par l'admin
    url('createAccountAdmin', views.createAccountAdminView, name = 'createAccountAdmin'),


### Pour ajouter le rapport
    url('addReport', views.addReportView, name = 'addReport'),


### Pour ajouter un article
    url('writeArticle', views.writeArticleView, name = 'writeArticle'),


### Pour afficher la liste des articles du doctorant
    url('mesArticles', views.mesArticlesView, name = 'mesArticles'),


### Pour afficher la liste des articles des doctorants
    url('articles', views.articlesView, name = 'articles'),


### Pour afficher la page des articles
    url('listArticles', views.listArticlesView, name = 'listArticles'),


### Pour supprimer un article
    url('deleteArticle/(?P<article_id>\d+)/$', views.deleteArticleView, name = 'deleteArticle'),


### Pour editer un article
    url('editArticle/(?P<article_id>\d+)/$', views.editArticleView, name = 'editArticle'),


### Pour lire un article
    url('readArticle/(?P<article_id>\d+)/$', views.readArticleView, name = 'readArticle'),


### Pour valider un article
    url('validArticle/(?P<article_id>\d+)/$', views.validArticleView, name = 'validArticle'),
]


### <app>/<model>_<viewtype>.html
