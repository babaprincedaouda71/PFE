from django import forms
from .models import individu
from .models import candidat
from .models import diplome
from datetime import datetime


### Class django pour afficher le calendrier au niveau du formulaire
class dateInput(forms.DateInput):
####Le formulaire pour l'inscription du candidat####
    input_type = 'date'
class registerForm(forms.Form):
    cin = forms.CharField(max_length = 8, label = "CIN")
    fname = forms.CharField(max_length = 50, label = "Nom")
    lname = forms.CharField(max_length = 50, label = "Prénom")
    photo = forms.ImageField(label = "Photo")
    email = forms.EmailField(max_length = 30, label = "Adresse mail")
    tel = forms.CharField(max_length = 15, label = "Téléphone")
    address = forms.CharField(max_length = 60, label = "Adresse")
    ville_residence = forms.CharField(max_length = 250, label = "Ville de résidence")
    genre = forms.ChoiceField(choices = [('M', 'Masculin'), ('F', 'Feminin')], label = "Genre")
    etat_civil = forms.ChoiceField(choices = [('Célibataire', 'Célibataire'), ('Marié/Mariée', 'Marié/Mariée')], label = "Etat civil")
    date_nais = forms.DateField(label = "Date de naissance", widget = dateInput)
    type_dip = forms.ChoiceField(choices = [('Master', 'Master'),("Diplome d'ingenieur", "Diplome d'ingenieur")], label = "Choisissez votre diplome")
    date_dip = forms.DateField(label = "Date du diplome", widget = dateInput)
    fonction = forms.CharField(max_length = 60, label = "Votre fonction")
    entreprise = forms.CharField(max_length= 60, label = "Le nom de l'entreprise")
    #body = forms.CharField(widget=forms.Textarea)

class PostForm(forms.ModelForm):

    class Meta:
        required_css_class = 'required'
        #model = diplome
        #model = candidat,
        model = individu
        #fields = ('code_dip', 'type_dip',)
    #    fields = ('date', 'fonction', 'entreprise')
        fields = ('cin', 'nom', 'prenoms', 'photo', 'mail', 'tel', 'addr', 'ville_residence', 'genre', 'etat_civil', 'date_nais')

class candidatForm(forms.ModelForm):
    class Meta:
        model = candidat
        fields = ('fonction', 'entreprise')


class diplomeForm(forms.ModelForm):
    class Meta:
        model = diplome
        fields = ('code_dip', 'type_dip', 'date_dip')


class testForm(forms.Form):
    nom = forms.CharField(max_length = 6, label = 'Nom')
    prenom = forms.CharField(max_length = 6, label = 'Prénom')
    email = forms.EmailField(max_length = 30, label = 'Adresse mail')




class diplomeCandidatForm(forms.Form):
    type_dip = forms.CharField(max_length = 100, label = 'Type du diplome')
    date_dip = forms.DateField(label = 'Date obtention du diplome')
    fonction = forms.CharField(max_length = 60, label = 'Fonction')
    entreprise = forms.CharField(max_length = 60, label = 'Entreprise')
