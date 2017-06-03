from django.shortcuts import render, get_object_or_404
from .models import *
from .other_function import *
from django.views.generic import TemplateView,ListView

class index_view(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(index_view, self).get_context_data(**kwargs)
        context['connected'] = self.request.user.is_authenticated()
        context['object_list']=self.request.POST.get("content")
        return context


class produits_view(ListView):
    template_name="produits.html"
    model=Produit
    paginate_by = 3
    def get_context_data(self, **kwargs):
        context = super(produits_view, self).get_context_data(**kwargs)
        context['connected'] = self.request.user.is_authenticated()
        return context


class projects_view(TemplateView):
    template_name = "projects.html"
    def get_context_data(self, **kwargs):
        context = super(projects_view, self).get_context_data(**kwargs)
        context['connected'] = self.request.user.is_authenticated()
        return context

class SAV_view(TemplateView):
    template_name = "SAV.html"
    def get_context_data(self, **kwargs):
        context = super(SAV_view, self).get_context_data(**kwargs)
        context['connected'] = self.request.user.is_authenticated()
        return context

class contact_view(TemplateView):
    template_name = "contact_us.html"
    def get_context_data(self, **kwargs):
        context = super(contact_view, self).get_context_data(**kwargs)
        context['connected'] = self.request.user.is_authenticated()
        return context


class produit_detail_view(TemplateView):
    template_name = "produit_detail.html"

    def get_context_data(self, **kwargs):
        context = super(produit_detail_view, self).get_context_data(**kwargs)
        context['connected'] = self.request.user.is_authenticated()
        context['instance'] = get_object_or_404(Produit, id_produit=self.kwargs['id'])
        return context
