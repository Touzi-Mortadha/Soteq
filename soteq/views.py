from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about_us.html")


def produit(request):
    return render(request, "produits.html")


def contact(request):
    return render(request, "contact_us.html")


def projets(request):
    return render(request, "projects.html")


def SAV(request):
    return render(request, "SAV.html")
