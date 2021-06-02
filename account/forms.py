from django import forms
from .models import my_user
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class my_registration_form(UserCreationForm):
    username = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()

    class Meta:
        model = my_user
        fields = ["username", "address", "email", "password1", "password2"]


class my_login_form(AuthenticationForm):
    pass