from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.sites.shortcuts import get_current_site
from .other_function import *
from django.views.generic import TemplateView,ListView
from django.views import View
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import *
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template






class index_view(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(index_view, self).get_context_data(**kwargs)
        context['object_list']=self.request.POST.get("content")
        return context

class produits_view(ListView):
    template_name="produits.html"
    model=Produit
    paginate_by = 8


#class projects_view(TemplateView):
#    template_name = "projects.html"

class SAV_view(TemplateView):
    template_name = "SAV.html"



class produit_detail_view(TemplateView):
    template_name = "produit_detail.html"

    def get_context_data(self, **kwargs):
        context = super(produit_detail_view, self).get_context_data(**kwargs)
        context['instance'] = get_object_or_404(Produit, id_produit=self.kwargs['id'])
        return context


class signup(View):
    form_class = SignUpForm
    template_name = 'signup.html'
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Soteq Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            toemail = form.cleaned_data.get('email')
            email = EmailMessage(subject, message, to=[toemail])
            email.send()
            return redirect('account_activation_sent')
        return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.userprofile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'account_activation_invalid.html')


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

class contact_view(View):
    form_class = ContactForm
    template_name = 'contact_us.html'
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_last_name = request.POST.get('contact_last_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')


            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_last_name': contact_last_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "Soteq a reçu un nouveau message",
                content,
                "Your website" +'',
                ['soteqapp@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')
        return render(request, self.template_name, {'form': form})
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})



class project_view(View):
    form_class = ProjectForm
    template_name = 'projects.html'
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            last_name = request.POST.get('last_name', '')
            email = request.POST.get('email', '')
            description = request.POST.get('description', '')


            template = get_template('project_template.txt')
            context = {
                'name': name,
                'last_name':last_name,
                'email': email,
                'form_description': description,
            }
            content = template.render(context)

            email = EmailMessage(
                "Soteq a reçu un nouveau projet",
                content,
                "Your website" +'',
                ['soteqapp@gmail.com'],
                headers = {'Reply-To': email }
            )
            email.send()
            return redirect('projet')
        return render(request, self.template_name, {'form': form})
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
