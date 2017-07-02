from .models import *
from django.db.models import Q
from itertools import chain
import re


def recherche(query):
    words = re.split(r"[^A-Za-z']+", query)
    q = Q()  # empty Q object
    for word in words:
        # 'or' the queries together
        q |= (Q(nom_produit__icontains=word) |
              Q(description__icontains=word) |
              Q(categorie__icontains=word))
    queryset_list1 = Produit.objects.filter(q).all()

    # queryset_list1 = Produit.objects.filter(
    #     Q(nom_produit__icontains=query) |
    #     Q(description__icontains=query) |
    #     Q(categorie__icontains=query)
    # ).distinct()



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
