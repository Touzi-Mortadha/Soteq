from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index', views.index),
    url(r'^about', views.about),
    url(r'^contact', views.contact),
    url(r'^projects', views.projets),
    url(r'^produits', views.produit),
    url(r'^SAV', views.SAV),

]
