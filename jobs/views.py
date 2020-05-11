from django.shortcuts import render

from.models import Job


def home(request):
    jobs = Job.objects #(This is to retrive the entire Job table from models.py. We need to import Job first (2nd line))
    return render(request, 'jobs/home.html', {'jobs':jobs})
