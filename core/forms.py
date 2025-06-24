from django import forms
from .models import Job
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Application

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
        
        
class ApplicationForm(forms.ModelForm):
    class Meta :
        model = Application
        fields =['resume','cover_letter']
    
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})