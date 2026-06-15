from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False, label='Телефон')
    address = forms.CharField(widget=forms.Textarea, required=False, label='Адрес')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address', 'password1', 'password2']