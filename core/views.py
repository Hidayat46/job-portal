from django.shortcuts import render , redirect
from django.shortcuts import render
from django.contrib.auth import authenticate , login , logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm
from django.contrib.auth.decorators import user_passes_test




def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.role == 'seeker':
                return redirect('seeker_dashboard')
            else:
                return redirect('employer_dashboard') 
    else:
        form = CustomUserCreationForm()

    return render(request, 'auth/signup.html', {'form': form})
            
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.role == 'seeker':
                return redirect('seeker_dashboard')
            else:
                return redirect('employer_dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'auth/login.html') 

    return render(request, 'auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def seeker_dashboard(request):
    return render(request, 'dashboard/seeker.html')

@login_required
def employer_dashboard(request):
    return render(request, 'dashboard/employer.html')

def is_employer(user):
    return user.is_authenticated and user.role == 'employer'

@user_passes_test(is_employer)
def post_job(request):
    if request .method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            return redirect(request, 'jobs/post_job.html',{'form':form})
        
@login_required
def job_list(request):
    jobs = job.objects.all().order_by('-created_at')
    return render(request , 'jobs/job_list.html',{'jobs':jobs})