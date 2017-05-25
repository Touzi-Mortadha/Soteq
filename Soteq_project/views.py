from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "About_us.html")


def produit(request):
    return render(request, "Produit.html")


def contact(request):
    return render(request, "Contact_us.html")


def projets(request):
    return render(request, "Projects.html")


def SAV(request):
    return render(request, "SAV.html")
