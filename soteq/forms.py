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
