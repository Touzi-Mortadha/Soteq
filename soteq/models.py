from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=100,blank=True)
    numero = models.IntegerField(blank=True,null=True)
    cin = models.IntegerField(blank=True,null=True) #this one is temporary
    email_confirmed = models.BooleanField(default=False)
    


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

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()
