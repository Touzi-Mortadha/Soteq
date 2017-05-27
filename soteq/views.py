from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain


def recherche(query):
    queryset_list1 = Produit.objects.all()  # +Projet.objects.all()
    # queryset_list2 = Projet.objects.all()
    queryset_list1 = queryset_list1.filter(
        Q(nom_produit__icontains=query) |
        Q(description__icontains=query) |
        Q(categorie__icontains=query)
    ).distinct()
    # queryset_list2 = queryset_list2.filter(
    #     Q(nom_projet__icontains=query) |
    #     Q(etude__icontains=query)
    # ).distinct()
    # queryset_list2 = chain(queryset_list1,queryset_list2)

    return queryset_list1


def is_connected(request):
    if not request.user.is_staff or not request.user.is_superuser:
        connected = 'false'
    else:
        connected = 'true'
    return connected


def index(request):
    connected = is_connected(request)

    query = request.POST.get("content")

    queryset_list = {}
    if query:
        queryset_list = recherche(query)
    context = {
        "connected": connected,
        "object_list": queryset_list,
    }
    return render(request, "index.html", context)


def produit(request):
    connected = is_connected(request)
    return render(request, "produits.html")


def contact(request):
    connected = is_connected(request)
    return render(request, "contact_us.html")


def projets(request):
    connected = is_connected(request)
    return render(request, "projects.html")


def SAV(request):
    return render(request, "SAV.html")
