from django import forms
from .models import individu
from .models import candidat
from .models import diplome


#class registerForm(forms.Form):
#    fname = forms.CharField()
#    lname = forms.CharField()
#    email = forms.EmailField()
#    category = forms.ChoiceField(choices = [('question', 'Question'), ('other', 'Other')])
#    subject = forms.CharField()
#    body = forms.CharField(widget=forms.Textarea)

class PostForm(forms.ModelForm):

    class Meta:
        #model = diplome
        #model = candidat,
        model = individu
        #fields = ('code_dip', 'type_dip',)
    #    fields = ('date', 'fonction', 'entreprise')
        fields = ('cin', 'nom', 'prenoms', 'photo', 'mail', 'tel', 'ville_residence', 'genre', 'etat_civil', 'date_nais')
        



"""class individuForm(forms.ModelForm):

    class Meta:
        model = individu
        fields = ('cin', 'nom', 'prenoms', 'photo', 'mail', 'tel', 'ville_residence', 'genre', 'etat_civil', 'date_nais')
"""
