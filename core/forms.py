from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=[
        ('seeker', 'Job Seeker'),
        ('employer', 'Employer')
    ])

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'role')
