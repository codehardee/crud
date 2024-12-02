from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'

class DataForm1(forms.ModelForm):
    class Meta:
        model = Datareceipe
        fields = '__all__'

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)

    class meta:
        model = User
        fields=('username', 'password1', 'password2', 'email', 'first_name', 'last_name')
    
    def save(self, commit=True):
        user=super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            return user
    