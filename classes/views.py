from django.shortcuts import render
from .models import AcademicClasses

# Create your views here.

from django.views.generic import ListView

class ClassView(ListView):
    template_name = 'course.html'
    queryset = AcademicClasses.objects.all()
