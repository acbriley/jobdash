from django.shortcuts import render, redirect
from dashboard.models import Job
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import User
# Create your views here.

# render page to show all jobs


def dashboard(req):
    jobs = Job.objects.all().order_by('pk')
    context = {
        "jobs": jobs,
    }
    return render(req, 'dashboard.html', context)

# render page for individual jobs


def job_detail(req, pk):
    job = Job.objects.get(pk=pk)
    context = {
        'job': job,
    }
    return render(req, 'job_detail.html', context)


def login_page(req):
    if req.method == 'POST':
        email = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, email=email, password=password)
        if user is not None:
            login(req, user)
            print('logged in')
            messages.info(req, 'You are now logged in')
            return redirect('dashboard')
        else:
            print('error logging in')
            messages.error(req, 'Invalid email or password')
    else:
        form = AuthenticationForm()
    return render(req, 'login.html', context={'form': form})


def signup(req):
    if req.method == 'POST':
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            print('valid user')
            form.save()
            return redirect('/')
            # return redirect('/myjobs')
        else:
            print(form.errors)
            return redirect('/')
    else:
        form = CustomUserCreationForm()

    form = CustomUserCreationForm
    return render(req, 'signup.html', context={'form': form})


def my_jobs(req):
    if req.user.is_authenticated:
        jobs = User.objects.values_list('jobs')
        context = {
            'jobs': jobs
        }
        return render(req, 'my_jobs.html', context)
    else:
        messages.info(req, 'You must be logged in to see this page.')
        return redirect('/')
