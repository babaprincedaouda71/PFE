#from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import PostForm
from .models import individu

# Create your views here.

def index(request):
    #return HttpResponse("<h1>Bienvenue a tous</h1>")
    return render(request, "home.html")


def register(request):
    """form = PostForm()
    return render(request, "pages/form.html", {'form': form})"""

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            individu_item = form.save(commit=False)
            individu_item.save()
            text = form_cleaned_data['form']
            return redirect('home')

    else:
        form = PostForm()
    return render(request, "pages/form.html", {'form': form})





def valid(request):
    return render(request, "pages/validation.html")


def about(request):
    return render(request, "pages/about.html")




def home(request):
    noms = individu.objects.all()
    return render(request, 'home.html', {'noms': noms})

"""def new_ind(request):
    if request.method=="POST":
        post_form = PostForm(request.POST)
        ind_form = individuForm(request.POST)

        if post_form.is_valid() and ind_form.is_valid():
            dipl = post_form.save()
            ind = ind_form.save(False)

            ind.dipl = dipl
            ind.save()

    else:
        post_form = PostForm()
        ind_form = individuForm()
    args = {}
    args.update(csrf(request))
    args['post_form'] = post_form
    args['ind_form'] = ind_form
    return render(request, "forms.html",args)
"""
