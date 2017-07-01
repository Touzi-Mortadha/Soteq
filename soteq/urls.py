from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index_view.as_view()),
    url(r'^index', views.index_view.as_view(), name="index"),
    url(r'^contact', views.contact_view.as_view(), name='contact'),
    url(r'^projects', views.project_view.as_view(), name='projet'),
    url(r'^produits', views.produits_view.as_view(), name='produits'),
    url(r'^SAV', views.SAV_view.as_view(), name='SAV'),
    url(r'^prod/(?P<id>\d+)/$', views.produit_detail_view.as_view(), name='detail'),
    url(r'^signup/$', views.signup.as_view(), name='signup'),
    url(r'^search/$', views.search_view.as_view(), name='search'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^story_1', views.story_view_1.as_view(), name="story_1"),
    url(r'^story_2', views.story_view_2.as_view(), name="story_2"),

    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    # views.activate, name='activate'),

]
