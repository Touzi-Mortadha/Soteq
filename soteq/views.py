from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .other_function import *
from django.views.generic import TemplateView

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
    number_of_object = queryset_list.count()
    number_of_object_in_page = 8

    number_pagination = (int)((number_of_object-1)/number_of_object_in_page) + 1
    s=''
    for i in range(number_pagination):
        s=s+'x'
    paginator = Paginator(queryset_list, number_of_object_in_page)  # Show 25 contacts per page

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
        "number_page": s ,
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




class SAV(TemplateView):
    template_name = "SAV.html"
# def SAV(request):
#     connected = is_connected(request)
#     context = {
#         "connected": connected,
#     }
#     return render(request, "SAV.html", context)
