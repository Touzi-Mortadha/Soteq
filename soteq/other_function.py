from .models import *
from django.db.models import Q
from itertools import chain

def recherche(query):
    queryset_list1 = Produit.objects.filter(
        Q(nom_produit__icontains=query) |
        Q(description__icontains=query) |
        Q(categorie__icontains=query)
    ).distinct()
    # queryset_list2 = Projet.objects.filter(
    #     Q(nom_projet__icontains=query)
    # ).distinct()
    # queryset_list2 = chain(queryset_list1,queryset_list2)
    return queryset_list1

def is_connected(request):
    if not request.user.is_staff or not request.user.is_superuser:
        connected = 'false'
    else:
        connected = 'true'
    return connected
