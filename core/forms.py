from django import forms
from .models import Job
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

class JobForm(forms.ModelForm):
    
    class Meta:
        model = Job
        fields =['title','description','location','category','salary']
        