#from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import PostForm
from .forms import diplomeForm
from .models import individu
from .forms import registerForm
from .forms import candidatForm
from .forms import diplomeCandidatForm
from .forms import testForm
from .models import test
from .models import diplome
from .models import candidat
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    #return HttpResponse("<h1>Bienvenue a tous</h1>")
    return render(request, "home.html")



#### Fonction pour la validation de l'inscription###
def registerFormView(request):
    submitted = False
    if request.method == 'POST':
        form = registerForm(request.POST, request.FILES)
        if form.is_valid():
            cin = request.POST['cin']
            fname = request.POST['fname']
            lname = request.POST['lname']
            try:
                photo = request.POST['photo']
            except MultiValueDictKeyError:
                photo = False
            email = request.POST['email']
            tel = request.POST['tel']
            address = request.POST['address']
            ville_residence = request.POST['ville_residence']
            genre = request.POST['genre']
            etat_civil = request.POST['etat_civil']
            date_nais = request.POST['date_nais']
            type_dip = request.POST['type_dip']
            date_dip= request.POST['date_dip']
            insertion2 = diplome(type_dip = type_dip, date_dip = date_dip)
            fonction = request.POST['fonction']
            entreprise = request.POST['entreprise']
            insertion3 = candidat(fonction = fonction, entreprise = entreprise)
            insertion1 = individu(cin = cin, nom = fname, prenoms = lname, photo = photo, mail = email, tel = tel, addr = address, ville_residence = ville_residence, genre = genre, etat_civil = etat_civil, date_nais = date_nais)
            insertion1.save()
            insertion2.save()
            insertion3.save()
            return redirect('pages:home')

    else:
        form = registerForm()
    return render(request, 'pages/inscription.html', {'form': form})



def register(request):
    submitted = False
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            cin = request.POST['cin']
            insertion = candidat(cin = cin)
            form.save()
            #return HttpResponseRedirect('/form/?submitted=True')
            return redirect('pages:diplomeCandidat')
            #return register1(request)


    else:
        form = PostForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "pages/form.html", {'form': form})


def register1(request):
    submitted = False
    if request.method == 'POST':
        form1 = diplomeForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            #form1.save()
            #return HttpResponseRedirect('/form/?submitted=True')
            return redirect('pages:home')
            #return register1(request)


    else:
        form1 = diplomeForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "pages/diplome.html", {'form1': form1})


#
def addDiplome(request):
    if request.method == "POST":
        form = diplomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:success')
        else:
            return redirect('pages:diplome')

    else:
        form = diplomeForm()
        return render(request, "pages/diplome.html", {'form': form})




def valid(request):
    return render(request, "pages/validation.html")


def about(request):
    return render(request, "pages/about.html")




def home(request):
    noms = individu.objects.all()
    return render(request, 'home.html', {'noms': noms})



def signup_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             return redirect('pages:home')
             #  now log the user in
             #user = User.objects.get(username=form.cleaned_data.get('username'))
            # login(request, user)
            # return redirect('articles:list') :You should add a home page here to redirect the user
    else:
        form = UserCreationForm()
    return render(request, 'pages/signup.html', { 'form': form })




def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user
            user = form.get_user()
            login(request,user)
            return redirect('pages:personalPage')
            # return redirect('articles:list') :You should add a personal page here to redirect the user to his page
    else:
        form = AuthenticationForm()
    return render(request, 'pages/login.html', { 'form': form })




def logout_view(request):
    if request.method == 'POST':
        logout(request)
    else:
        return redirect('pages:login')





def testView(request):
    if request.method == "POST":
        form = testForm(request.POST)
        if form.is_valid():
            nom = request.POST['nom']
            prenom = request.POST['prenom']
            email = request.POST['email']
            insertion = test(fname = nom, lname = prenom, mail = email)
            insertion.save()
            return redirect('pages:home')
    else:
        form = testForm()
    return render(request, 'pages/test.html', {'form': form})



def diplomeCandidatView1(request):
    if request.method == "POST":
        form = diplomeCandidatForm(request.POST)
        if form.is_valid():
            type_dip = request.POST['type_dip']
            date_dip = request.POST['date_dip']
            insertion1 = diplome(type_dip = type_dip, date_dip = date_dip)
            insertion1.save()
            fonction = request.POST['fonction']
            entreprise = request.POST['entreprise']
            insertion2 = candidat(fonction = fonction, entreprise = entreprise)
            insertion2.save()
            return redirect('pages:home')
    else:
        form = diplomeCandidatForm()
    return render(request, 'pages/diplomeCandidat.html', {'form': form})


@login_required(login_url="/pages/login/")
def personalPageView(request):
    individus = individu.objects.all()
    diplomes = diplome.objects.all()
    candidats = candidat.objects.all()
    return render(request, "pages/personalPage.html", {'individus': individus})


#def diplomeCandidatView2(request):
    #if request.method == "POST":
        #form = diplomeCandidatForm(request.POST)
        #if form.is_valid():
#            type_dip = request.POST['type_dip']
#            date_dip = request.POST['date_dip']
#            insertion1 = diplome(type_dip = type_dip, date_dip = date_dip)
#            insertion1.save()
        #if form.is_valid():
#            fonction = request.POST['fonction']
#            entreprise = request.POST['entreprise']
#            insertion2 = candidat(fonction = fonction, entreprise = entreprise)
#            insertion2.save()

            #test.objects.fname = 'nom'
            #test.objects.lname = 'prenom'
            #test.objects.mail = 'email'
            #return redirect('pages:home')
    #else:
    #    form = diplomeCandidatForm()
    #return render(request, 'pages/diplomeCandidat.html', {'form': form})
