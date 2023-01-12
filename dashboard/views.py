from django.shortcuts import render
from dashboard.models import Job
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
