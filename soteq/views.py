from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .other_function import *


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
    # query = request.POST.get("content")
    # queryset_list = {}
    # if query:
    #     queryset_list = recherche(query)
    queryset_list = Produit.objects.all()

    paginator = Paginator(queryset_list, 8)  # Show 25 contacts per page

    page_request_var = "page"

    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    connected = is_connected(request)
    context = {
        "object_list": queryset_list,
        "connected": connected,
        "produit": queryset,
        "page_request_var": page_request_var,
    }
    return render(request, "produits.html", context)


def produit_detail(request, id=None):
    instance = get_object_or_404(Produit, id_produit=id)
    connected = is_connected(request)
    context = {
        "connected": connected,
        "instance": instance,
    }
    return render(request, "produit_detail.html", context)


def contact(request):

    connected = is_connected(request)
    context = {
        "connected": connected,
    }
    return render(request, "contact_us.html", context)


def projets(request):
    connected = is_connected(request)
    context = {
        "connected": connected,
    }
    return render(request, "projects.html", context)


def SAV(request):
    connected = is_connected(request)
    context = {
        "connected": connected,
    }
    return render(request, "SAV.html", context)
