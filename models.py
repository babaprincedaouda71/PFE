from django.db import models
#from django.utils import timezone
from datetime import datetime


# Create your models here.


class individu(models.Model):
    cin = models.CharField(max_length = 8, primary_key = True, default = "")
    nom = models.CharField(max_length = 100, default="")
    prenoms = models.CharField(max_length = 42, default="")
    photo = models.ImageField(default="")
    mail = models.EmailField(max_length = 30, default='exemple@gmail.com')
    tel = models.CharField(max_length = 15, default="")
    addr = models.CharField(max_length = 60, default="")
    ville_residence = models.CharField(max_length = 250, default="")
    username = models.CharField(max_length = 30, default="")
    password = models.CharField(max_length = 15, default="")
    genre_choice = (
        ('Masculin', 'Masculin'),
        ('Feminin', 'Feminin'),
    )
    genre = models.CharField(max_length = 15, choices = genre_choice)
    civil_choice = (
        ('Celibataire', 'Celibataire'),
        ('Marié', 'Marié'),
        ('Veuf/Veuve', 'Veuf/Veuve'),
    )
    etat_civil = models.CharField(max_length = 15, choices = civil_choice)
    date_nais = models.DateField(default=datetime.now)
    est_admin = models.BooleanField(default=False)




class candidat(models.Model):
    num_insc = models.AutoField(primary_key = True)
    date = models.DateTimeField()
    fonction = models.CharField(max_length = 60)
    entreprise = models.CharField(max_length = 60)




class diplome(models.Model):
    diplome_choice = (
        ('mst001', 'mst001'),
        ('mst002', 'mst002'),
        ('ing001', 'ing001'),
    )
    code_dip = models.CharField(max_length=20, choices = diplome_choice, primary_key = True)
    type_dip = models.CharField(max_length=100, default="")
    date_dip = models.DateTimeField()
    libelle_dip = models.CharField(max_length=100, default="")




class these(models.Model):
    id_these = models.AutoField(primary_key = True)
    titre_these = models.CharField(max_length=100, default="")



class compte(models.Model):
    ref_compte = models.AutoField(primary_key = True)
    date_cree = models.DateTimeField()




class doctorant(models.Model):
    id_doctorant = models.AutoField(primary_key = True)
    date_dip = models.DateTimeField()
    id_these= models.ForeignKey(these, on_delete=models.CASCADE)
    ref_compte= models.ForeignKey(compte, on_delete=models.CASCADE)
    num_insc = models.ForeignKey(candidat, on_delete=models.CASCADE)





class professeur(models.Model):
    code_prof = models.AutoField(primary_key = True)
    status = models.BooleanField(default = False)
    ref_compte= models.ForeignKey(compte, on_delete=models.CASCADE)
    id_doctorant = models.ForeignKey(doctorant, on_delete=models.CASCADE)



class equipe_recherche(models.Model):
    id_equipe = models.AutoField(primary_key = True)
    libelle_equipe = models.CharField(max_length=100, default="")
    code_prof= models.ForeignKey(professeur, on_delete=models.CASCADE)
    id_doctorant = models.ForeignKey(doctorant, on_delete=models.CASCADE)



class labo(models.Model):
    labo_choice = (
        ('001', '001'),
        ('002', '002'),
    )
    id_labo = models.CharField(max_length=100, primary_key = True, choices = labo_choice)
    libelle_labo = models.CharField(max_length=100, default="")
    id_equipe = models.ForeignKey(equipe_recherche, on_delete=models.CASCADE)



class enregistrement(models.Model):
    id_enregistrement = models.AutoField(primary_key = True)
    rapport = models.CharField(max_length=100, default="")
    articles = models.CharField(max_length=100, default="")
    date_enregristrement = models.DateTimeField()





class posseder_dip(models.Model):
    code_dip = models.ForeignKey(diplome, on_delete = models.CASCADE)
    id_doctorant = models.ForeignKey(doctorant, on_delete = models.CASCADE)



class jury(models.Model):
    code_jury = models.AutoField(primary_key = True)
    libelle_jury =  models.CharField(max_length=100, default="")
    code_prof= models.ForeignKey(professeur, on_delete=models.CASCADE)



class admin(models.Model):
    id_admin = models.AutoField(primary_key = True)
    ref_compte= models.ForeignKey(compte, on_delete=models.CASCADE)
    code_jury= models.ForeignKey(jury, on_delete=models.CASCADE)
