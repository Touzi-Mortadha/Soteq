from django.shortcuts import render, get_object_or_404
from .models import *
from .other_function import *
from django.views.generic import TemplateView,ListView

class index_view(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(index_view, self).get_context_data(**kwargs)
        context['object_list']=self.request.POST.get("content")
        return context

class produits_view(ListView):
    template_name="produits.html"
    model=Produit
    paginate_by = 3

class projects_view(TemplateView):
    template_name = "projects.html"

class SAV_view(TemplateView):
    template_name = "SAV.html"


class contact_view(TemplateView):
    template_name = "contact_us.html"



class produit_detail_view(TemplateView):
    template_name = "produit_detail.html"

    def get_context_data(self, **kwargs):
        context = super(produit_detail_view, self).get_context_data(**kwargs)
        context['instance'] = get_object_or_404(Produit, id_produit=self.kwargs['id'])
        return context
