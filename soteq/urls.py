from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^index', views.index,name='index'),
    url(r'^contact', views.contact,name='contact'),
    url(r'^projects', views.projets,name='projet'),
    url(r'^produits', views.produit,name='produits'),
    url(r'^prod/(?P<id>\d+)/$',views.produit_detail,name='detail'),
    url(r'^SAV', views.SAV.as_view(),name='SAV'),
]
