from django.db import models
#from django.utils import timezone
from datetime import datetime


# Create your models here.


class individu(models.Model):
    code = models.CharField(max_length = 5, primary_key=True, default="")
    nom = models.CharField(max_length = 100, default="")
    prenoms = models.CharField(max_length = 42, default="")
    photo = models.ImageField(default="")
    mail = models.EmailField(max_length = 30, default='exemple@gmail.com')
    tel = models.CharField(max_length = 15, default="")
    addr = models.CharField(max_length = 60, default="")
    ville_residence = models.CharField(max_length = 250, default="")
    username = models.CharField(max_length = 30, default="")
    password = models.CharField(max_length = 15, default="")
    etat_civil = models.CharField(max_length = 15, default="")
    genre_choice = (
        ('Celibataire', 'Celibataire'),
        ('Marié', 'Marié'),
        ('Veuf/Veuve', 'Veuf/Veuve'),
    )
    genre = models.CharField(max_length = 20, choices = genre_choice)
    date_nais = models.DateField(default=datetime.now)
    est_admin = models.BooleanField(default=False)

"""class candidat(models.Model):
    num = models.CharField(max_length = )
    date
    fonction"""


"""class diplome(models.Model):
code_dip = models.CharField(max_length=100, default="")
type_dip = models.CharField(max_length=100, default="")
date_dip = models.DateTimeField()
libelle_dip = models.CharField(max_length=100, default="")


class these(models.Model):
id_these = models.CharField(max_length=100, default="")
titre_these = models.CharField(max_length=100, default="")


class labo(models.Model):
id_labo = models.CharField(max_length=100, default="")
libelle_labo = models.CharField(max_length=100, default="")


class enregistrement(models.Model):
id_enregistrement = models.CharField(max_length=100, default="")
rapport = models.CharField(max_length=100, default="")
articles = models.CharField(max_length=100, default="")
date_enregristrement = models.DateTimeField()


class equipe_rechere(models.Model):
id_equipe = models.CharField(max_length=100, default="")
libelle_equipe = models.CharField(max_length=100, default="")
"""

class posseder_dip
