from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$',views.index_view.as_view()),
    url(r'^index',views.index_view.as_view(),name="index"),
    url(r'^contact',views.contact_view.as_view(),name='contact'),
    url(r'^projects',views.projects_view.as_view(),name='projet'),
    url(r'^produits', views.produits_view.as_view(),name='produits'),
    url(r'^SAV', views.SAV_view.as_view(),name='SAV'),
    url(r'^prod/(?P<id>\d+)/$',views.produit_detail_view.as_view(),name='detail'),

]
