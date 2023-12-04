# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from elearning_app.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']
