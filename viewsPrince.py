#from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import PostForm
from .forms import diplomeForm
from .models import individu, test, diplome, candidat
from .forms import registerForm
from .forms import candidatForm
from .forms import diplomeCandidatForm
from .forms import testForm
from .forms import createAccountForm
#from .forms import userLoginForm
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

# Create your views here.

def index(request):
    #return HttpResponse("<h1>Bienvenue a tous</h1>")
    return render(request, "general/home.html")


#@user_passes_test(lamda u: u.is_superuser)
def admintemp(request):
    return render(request, "pages/admintemp.html")



#### Fonction pour la validation de l'inscription###
@login_required(login_url="/accounts/login/")
def registerFormView(request):
    submitted = False
    if request.method == 'POST':
        form = registerForm(request.POST, request.FILES)
        if form.is_valid():
            cin = request.POST['cin']
            fname = request.POST['fname']
            lname = request.POST['lname']
            #try:
            photo = request.POST['photo']
            #except MultiValueDictKeyError:
                #photo = False
            email = request.POST['email']
            tel = request.POST['tel']
            address = request.POST['address']
            ville_residence = request.POST['ville_residence']
            genre = request.POST['genre']
            etat_civil = request.POST['etat_civil']
            date_nais = request.POST['date_nais']
            type_dip = request.POST['type_dip']
            date_dip= request.POST['date_dip']
            insertion1 = individu(cin = cin, nom = fname, prenoms = lname, photo = photo, mail = email, tel = tel, addr = address, ville_residence = ville_residence, genre = genre, etat_civil = etat_civil, date_nais = date_nais)
            insertion1.save()
            insertion2 = diplome(type_dip = type_dip, date_dip = date_dip)
            insertion2.save()
            fonction = request.POST['fonction']
            entreprise = request.POST['entreprise']
            insertion3 = candidat(fonction = fonction, entreprise = entreprise, cine = cin)
            insertion3.save()
            return redirect('pages:home')

    else:
        form = registerForm()
    return render(request, 'general/register.html', {'form': form})



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
    #noms = individu.objects.all()
    return render(request, "general/home.html")



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




# Creation de compte
def createAccountView(request):
    #form = UserCreationForm()
    if request.method == 'POST':
         form = createAccountForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request, f'Le compte est cree! Vous pouvez vous conecter')
             #user = form.save()
             return redirect('pages:login')
             #  now log the user in
             #user = User.objects.get(username=form.cleaned_data.get('username'))
            # login(request, user)
            # return redirect('articles:list') :You should add a home page here to redirect the user
    else:
        form = createAccountForm()
    return render(request, 'general/createAccount.html', { 'form': form })



### fonction pour afficher le profile de l'utilisateur
@login_required
def profile(request):
    return render(request, "general/profile.html")



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


# Login Function
def loginView(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user
            user = form.get_user()
            login(request,user)
            #if user.is_superuser:
            #return redirect('pages:admintemp')
            #else:
            return redirect('pages:home')
            # return redirect('articles:list') :You should add a personal page here to redirect the user to his page
    else:
        form = AuthenticationForm()
    return render(request, 'general/login.html', { 'form': form })




def loginAsAdminView(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user
            user = form.get_user()
            login(request,user)
            if user.is_superuser:
                return redirect('pages:admintemp')
            # return redirect('articles:list') :You should add a personal page here to redirect the user to his page
    else:
        form = AuthenticationForm()
    return render(request, 'general/login.html', { 'form': form })





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


#@login_required(login_url="/pages/login/")
def personalPageView(request):
    individus = individu.objects.all()
    #diplomes = diplome.objects.all()
    #candidats = candidat.objects.all()
    return render(request, "general/test.html", {'individus': individus})

def preSelectionView(request):
    individus = individu.objects.all()
    return render(request, "general/preSelection.html", {'individus': individus})

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


    """
    def userLoginView(request):
        next = request.GET.get('next')
        form = userLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            login(request, user)
            if next:
                return redirect(next)
                return redirect('/')
                # Avec ca je peux afficher des champs de tables diffrentes
                context = {
                'form': form,
                }
                return render(request, "general/login.html", context)

                def userRegisterView(request):
                    next = request.GET.get('next')
                    form = userLoginForm(request.POST or None)
                    if form.is_valid():
                        username = form.cleaned_data.get('username')
                        password = form.cleaned_data.get('password')
                        user = authenticate(username = username, password = password)
                        login(request, user)
                        if next:
                            return redirect(next)
                            return redirect("pages:home")
                            # Avec ca je peux afficher des champs de tables diffrentes
                            context = {
                            'form': form,
                            }
                            return render(request, "general/login.html", context)
                            """
