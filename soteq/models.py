from django.db import models
from django.core.urlresolvers import reverse



def upload_location(instance, filename):
    return "%s/%s" %(instance.id_produit,filename)



class Produit(models.Model):
    id_produit = models.AutoField(primary_key=True)
    categorie = models.CharField(max_length=100)
    nom_produit = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    images0 = models.ImageField(upload_to=upload_location)
    images1 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    images2 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    images3 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    images4 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    fichiers = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.nom_produit

    def get_absolute_url(self):
        return reverse("detail",kwargs={"id":self.id_produit})
        # return "/prod/%s" % (self.id_produit)


class categorie(models.Model):
    id_categorie = models.AutoField(primary_key=True)
    nom_categorie = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom_categorie


class user(models.Model):
    id_user = models.AutoField(primary_key=True)
    type_user_choices = (('AD', 'Admin'), ('CL', 'Client'))
    type_user = models.CharField(max_length=10, choices=type_user_choices, default='Client')
    nom = models.CharField(max_length=10)
    prenom = models.CharField(max_length=10)
    adresse = models.CharField(max_length=100)
    numero = models.IntegerField()
    email = models.EmailField()
    cin = models.IntegerField()

    def __str__(self):
        return self.nom


class Projet(models.Model):
    id_projet = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    nom_projet = models.CharField(max_length=50)
    etude = models.FileField(null=True, blank=True)
    date_soumission = models.DateField(auto_now_add=True)
    etat_choices = (('E', 'En_etude'), ('A', 'Accepte'), ('R', 'Refuse'))
    etat = models.CharField(max_length=10, choices=etat_choices, default='En_etude')

    def __str__(self):
        return self.nom_projet
