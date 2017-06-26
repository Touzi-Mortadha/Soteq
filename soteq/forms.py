from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control input-lg'})
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control input-lg'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control input-lg'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control input-lg'})
        self.fields['password1'].widget.attrs.update({'class' : 'form-control input-lg'})
        self.fields['password2'].widget.attrs.update({'class' : 'form-control input-lg'})


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_last_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Votre Nom:"
        self.fields['contact_last_name'].label = "Votre Prénom:"
        self.fields['contact_email'].label = "Votre Mail:"
        self.fields['content'].label = "Laissez votre message:"


class ProjectForm(forms.Form):
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    description = forms.CharField(required=True, widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Votre Nom:"
        self.fields['last_name'].label = "Votre Prénom:"
        self.fields['email'].label = "Votre Mail:"
        self.fields['description'].label = "Laissez une description de votre projet:"
        self.fields['name'].widget.attrs.update({'class' : 'form-control form-group col-lg-12'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control form-group col-lg-12'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control form-group col-lg-12'})
        self.fields['description'].widget.attrs.update({'class' : 'form-control form-group col-lg-12'})
