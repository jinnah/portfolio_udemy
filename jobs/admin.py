from django.contrib import admin
# MJ -  Here we are importing <Job> model (Class name) from models.py
from .models import Job


# MJ - Now we need to register the app to show in the admin panel
admin.site.register(Job)