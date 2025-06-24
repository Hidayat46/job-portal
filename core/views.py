from django.shortcuts import render , redirect
from django.shortcuts import render
from django.contrib.auth import authenticate , login , logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm
from django.contrib.auth.decorators import user_passes_test
from .models import Job, Application
from .forms import ApplicationForm
from django.shortcuts import render, get_object_or_404, redirect



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
    form = JobForm()
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            return redirect('employer_dashboard')
    
    return render(request, 'jobs/post_jobs.html', {'form': form})
        
@login_required
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.seeker = request.user 
            application.save()
            return redirect('seeker_dashboard')
    else:
        form = ApplicationForm()

    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})


@user_passes_test(is_employer)
def view_applicants(request, job_id):
    job = Job.objects.get(id=job_id, employer=request.user)
    applicants = Application.objects.filter(job=job)

    return render(request, 'jobs/view_applicants.html', {'job': job, 'applicants': applicants})
